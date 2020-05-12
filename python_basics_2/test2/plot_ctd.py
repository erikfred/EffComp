"""
Code to import and plot CTD data from a text file.
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
import matplotlib.pyplot as plt

depth_list=[]
temp_list=[]

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
out_fn = out_dir + 'out_tempVdepth.txt'

# open the output file for writing
outfile = open(out_fn, 'w')

# create a dict for translating direction letters to numbers
sign_dict = {'N':1,'S':-1,'E':1,'W':-1}

# go through the input file one line at a time, and just
# write decimal versions of the latitude and longitude
# to the output file
with open(in_fn, 'r', errors='ignore') as f:
    # typical real-world issue: the read operation throws an error
    # around line 383 for unknown reasons - we ignore it.
    n=0
    for line in f:
        n+=1
        if n>=571:
            LS = line.split() # .split() makes a list out of the separate items in line
            d = -1 * float(LS[1])
            T = float(LS[2])
            # have to turn text things into numbers using float([string])
            depth_list.append(d)
            temp_list.append(T)
            # write a line to the outfile
            outfile.write('d = %0.3f m, T = % 0.3f C\n' % (d,T))
            # and write to the screen
            print('d = %0.3f m, T = % 0.3f C' % (d,T))

# close the output file
outfile.close()

# plotting

plt.plot(temp_list,depth_list)
plt.ylabel('depth (m)')
plt.xlabel('temperature (C)')
plt.show()

plt.savefig(out_dir + 'out_test1.png')
