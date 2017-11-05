#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:21:44 2017

@authors: 
"""

# Python library imports.
import sys
import os
import string
import subprocess

# BioPython module imports.
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

################################################################################
############################### MAIN PROGRAM ###################################
################################################################################

input_filename = "SRS015374.denovo_duplicates_marked.trimmed.singleton.fastq"


try:
   # Read the input FASTA file using BioPython...
   with open(input_filename, "r" ) as Infile:
       
       for record in SeqIO.parse( Infile, "fastq" ):

      # Launch a remote BLAST ...
          print( "Lanching BLASTN..." )
          database = "nt"  ## Nucleotide database
          hit_size = 10 # hitlist_size
          threshold = 1.0 #expect=10.0
          result_handle = NCBIWWW.qblast("blastn", database, record.seq,
                                         hitlist_size=10, expect=1.0,
                                         alignments=10 )

          print( "Parsing records..." )
          blastn_records = list( NCBIXML.parse(result_handle) )
          
          blast_record = next(blastn_records)
          
          for hsp in blast_record.alignments[0].hsps: 
              print( "Expect: ", hsp.expect )
              print( "Ident: ", hsp.identities )
              hsp
     # end for
  
    # end with
  
except IOError as error:
   print( "Error:", str(error) )





