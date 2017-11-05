#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:21:44 2017

@authors: 
"""
import os

# BioPython module imports.
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


################################################################################
############################### MAIN PROGRAM ###################################
################################################################################

input_filename = "Fusobacteriumalign.fasta"


try:
   # Read the input FASTA file using BioPython...
   with open(input_filename, "r" ) as Infile:
          
       trim = 60
       base = os.path.splitext(input_filename)[0]
       output_name = base + "trim" + str(trim) + ".txt"
       
       output_file = open( output_name, "w" )
                 
       for record in SeqIO.parse( Infile, "fasta" ):
      
       ##   print( record.seq )

          
          if len(record.seq) >= trim:
             trimmed = str(record.seq[0:trim])
             print( "writing: ", trimmed )
             output_file.write( trimmed + "\n" )
    

       # end for
       output_file.close()
    # end with
  
except IOError as error:
   print( "Error:", str(error) )





