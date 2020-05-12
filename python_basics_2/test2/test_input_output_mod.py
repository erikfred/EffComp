"""
Code to test input and (filtered) output of a text file.
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod

myplace = 'test2' # *** YOU NEED TO EDIT THIS ***

# input directory
in_dir = '../' + myplace + '_data/'

# make sure the output directory exists
out_dir = '../' + myplace + '_output/'
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + '2017-01-0118.ctd'
# this is some Canadian CTD data, formatted in a strict but
# difficult-to-use way

# define the output filename
out_fn = out_dir + 'out_test.txt'

# open the output file for writing
outfile = open(out_fn, 'w')
