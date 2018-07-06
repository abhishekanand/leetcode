# -*- coding: utf-8 -*-
"""
Program DocString
Given a string , find ASII equivalent of the string 

EXample : string  = "ABC"
        output  = 65+66+67 = 198

"""
import sys


def asciisum(mystring):
    """
     Function Docstring
    """
    result = 0
    for c in mystring:
        result = result + ord(c)
    return result

if __name__ == "__main__":
    inputstring = "ABC"
    out = asciisum(inputstring)
    print(out)

 #print(sum(map(ord,inputstring))) # One Line to solve the issue 
 