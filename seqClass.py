#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args() #Using the parser function

args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq): #Searching the ACGTU letters in the sequence, if there are other letters, we're gonna get the "error" message : The sequence is not DNA nor RNA 
    if re.search('T', args.seq) and not re.search ('U', args.seq): #Get the sequences that contain T and not U.  
        print ('The sequence is DNA') #We're gonna get this message if the sequence contains a T
elif re.search('U', args.seq) and not re.search ('T', args.seq): #Get the sequences that contain U and not T
        print ('The sequence is RNA') #We're gonna get this message if the sequence contains a U
    else:
        print ('The sequence can be DNA or RNA') #If the sequence does not contain a T or U, it could be either DNA or RNA. This message will appear. 
else:
    print ('The sequence is not DNA nor RNA') #If the sequence does contain a letter which is not AUGCT, this message will appear


if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("The motif was FOUND") #When the sequence contains the introduced motif, this message will appear
    else:
        print("The motif was NOT FOUND")#If the sequence does not contain the introduced motif, this message will appear

