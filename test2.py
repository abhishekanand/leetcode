# -*- coding: utf-8 -*-
"""
Program DocString

"""
import sys


def indexValue(i_array, target):
    """
     Function Docstring
    """
    if(len(i_array) <= 2):
        return False
    else:
        for i in range(len(i_array)):
            first_index = i
            j = i + 1
            for j in range(len(i_array)):
                if i_array[i] + i_array[j] == target:
                    second_index = j
                    return [first_index, second_index]
    return False


if __name__ == "__main__":
    inputArray = [2, 7, 10, 11]
    target = 13
    out = indexValue(inputArray, target)
    print(out)
