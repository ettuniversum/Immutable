#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:21:44 2017

@authors: 
"""

# Python library imports.

import string
import numpy


################################################################################
############################### MAIN PROGRAM ###################################
################################################################################

input_filenames = ["genomes_proks.txt",
                   "genomes_proks-2.txt",
                   "genomes_proks-3.txt",
                   ##"genomes_proks-4.txt",  ## looks bad
                   "genomes_proks-5.txt",
                   "genomes_proks-6.txt"
                  ]
try:
   print 
   for filename in input_filenames:
      ## print "reading : " , filename
       data_type = str
       data = numpy.loadtxt( filename, data_type, delimiter="\t" )
                
       for i in range(0,data.shape[0]):       
          print (data[i,0]).split()[0], "," , float(data[i,9])
   print
   
except IOError as error:
   print "Error:", str(error)





