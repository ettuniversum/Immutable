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

input_filename = "SRS015374.denovo_duplicates_marked.trimmed.singleton.fastq"


try:
   # Read the input FASTA file using BioPython...
   with open(input_filename, "r" ) as Infile:
          
       bacterial_count = 0
       human_count = 0
       total = 0
       

    # Loop over each record in the input file..             
       for record in SeqIO.parse( Infile, "fastq" ):
       # Apply a series of tests based  on known human or bacterial DNA subsequences
       # eg. promoter regions
       
          bacterial = False
          human = False
         
          if "TATAAT" in record.seq:
              bacterial = True
          if "TTGACA" in record.seq:
              bacterial = True
          if "CGCG" in record.seq:
              bacterial = True
          if  "CCGG" in record.seq:
              bacterial = True
          if   "CCCGGG" in record.seq:
              bacterial = True
              
              
          if "TATAAA" in record.seq:
              human = True
          if "CACGTG" in record.seq:
              human = True
          if "AGCT" in record.seq:
              human = True
          if "TTAGGG" in record.seq:
              human = True
          if "GAAATCTGAT" in record.seq:
              human = True
          if "ATCGGAGAAC" in record.seq:
              human = True
          if "N" in record.seq:
              human = True

              
          if human :
              human_count += 1
          if bacterial :
              bacterial_count += 1
              
          total += 1
       # end for

    # end with
    
   print()
   print( "Bacterial count: ", bacterial_count )
   print( "Human count: " , human_count )
   print( "total count: " , total )
   
except IOError as error:
   print( "Error:", str(error) )





