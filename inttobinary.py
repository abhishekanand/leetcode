# -*- coding: utf-8 -*-
"""
Program DocString
Convert a given integer to it binary quivalent 
num =10 
output 1010



"""
import sys



def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])


if __name__ == "__main__":
    inputInteger = 4
    print(bin(inputInteger))
    print('{0:b}'.format(inputInteger))
    print (toBinary(inputInteger))
