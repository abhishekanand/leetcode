# -*- coding: utf-8 -*-
"""
Program DocString

"""
import sys

def maxintegervalue(input):
    """
     Function Docstring 
    """
    totalsum = 0
    totalmult= 1
    negative=False
    for c in input: # Reading one character at a time
        if c == '-':  # cheking 
            negative=True
        else:
            totalsum += int(c)
            totalmult *= int(c)

    if negative is True:
        totalsum = -1*totalsum
        totalmult = -1*totalmult
    return max(totalsum,totalmult)

if __name__ == "__main__":
    name = input("Please enter a number: ")
    out = maxintegervalue(str(name))
    print(out)
    ''' 
    for element in sys.argv:
        print(element)
    '''
