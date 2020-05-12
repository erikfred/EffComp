"""
Practice code for Class 506, 4/21/2020
"""

# dir(list)
# help(list.append)

our_list=['a string',92,'more words',420,'baby']

our_list.append('cute dog')
# whats the difference between append and extend?

b=our_list.count(92) #b = 1 here, counts number of occurences

c= our_list.index('a string') # c=0 returns index of a value

d = our_list.pop(3) # remove and return item selected to new variable

g = our_list.remove(92) # jsut remove that value

f = our_list.reverse()

g = our_list.sort() # only works when list is one type of thing (str or int)

# a=b a is just pointing to b so a will change when b changes
# a=b.copy will make a new and independent variable