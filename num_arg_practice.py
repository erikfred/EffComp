"""
Code for practicing with numpy and argparse

Usage:
run num_arg_practice -m 2.5 -p True
"""

# imports
import sys, os
import numpy as np
import pickle
import argparse

# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

def boolean_string(s):
    # this function helps with getting Boolean input
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True' # note use of ==

# create the parser object
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--multiplier', default='hi', type=float)
parser.add_argument('-p', '--printout', default=True, type=boolean_string)

# get the arguments
args = parser.parse_args()

# make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
out_dir = '../' + this_dir + '_output/'
mymod.make_dir(out_dir)

# make my array
expenses = np.array([24.10, 11.99, 100, 3.95, 68.41])*args.multiplier

# I had to buy the same things the following day
updated_expenses = expenses.repeat(2)

# it's a long array now so let's break it up with an additional row
reshaped_expenses = updated_expenses.reshape(2,5)

# round the values so I don't have to deal with coind
round_expenses = reshaped_expenses.round()

# I changed my mind and now want a 1D array
flat_expenses = round_expenses.flatten()

# unsure why I would want to do this, but it's an interesting function
# NOTE: I couldn't figure out how to get partitioned_expenses.partition() to work
partitioned_expenses = np.partition(flat_expenses,3)

# get all my arrays into a single dict
ledger = {'Expenses' : expenses, 'Updated Expenses' : updated_expenses,
'Reshaped Expenses' : reshaped_expenses, 'Round Expenses' : round_expenses,
'Flat Expenses' : flat_expenses, 'Partitioned Expenses' : partitioned_expenses}

# pickle and save the dict
out_fn = out_dir + 'ledger.p'
pickle.dump(ledger, open(out_fn, 'wb')) # 'wb' is for write binary

# reload pickles
b = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary

# print info to console if requested
if args.printout:
    print('\nExpenses:')
    print(ledger['Expenses'])
    print('\nUpdated Expenses:')
    print(ledger['Updated Expenses'])
    print('\nReshaped Expenses:')
    print(ledger['Reshaped Expenses'])
    print('\nRound Expenses:')
    print(ledger['Round Expenses'])
    print('\nFlat Expenses:')
    print(ledger['Flat Expenses'])
    print('\nPartitioned Expenses:')
    print(ledger['Partitioned Expenses'])
