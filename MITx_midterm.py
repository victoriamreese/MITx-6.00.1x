#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 09:06:22 2018

@author: vicky
"""




def lessThan4(aList):
    '''
    aList: a list of string
    '''
    return [i for i in aList if len(i) < 4]

def closest_power(base, num):  
   #starting exponent 
    exp1 = 0
    if num != 1 and num != base:
        found = False
        while not found:
            test1 = base ** exp1
            exp2 = exp1 + 1
            test2 = base ** exp2
            if abs(num - test1) <= abs(num - test2):
                found = True
            else:
                exp1 = exp2
        else:
            print(exp1)
    elif num == 1:
        print(0)
    elif num == base:
        print(1)


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    toRemove= []
    testDict = aDict.copy()
    for key, value in aDict.items():
        del testDict[key]
        newvals = list(testDict.values())
        if value in set(newvals):
            toRemove.append(key)
            testDict = aDict.copy()
            print(toRemove)
        else:
            testDict = aDict.copy()
            continue
    for i in toRemove:
        del aDict[i]
    
    return dict(sorted(aDict.items()))
            

def general_poly(L):
    k = len(L)-1
    def poly(x):
        number = 0
        n = 0
        for _ in enumerate(L):
            number += (L[n]*(x**(k-n)))
            n += 1 
        return number
    return poly


def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            print((out+s2))
            return str(out + s2)
        if s2 == '':
            print((out+s1))
            return str(out + s1)
        else:
            helpLaceStrings(s1[1:], s2[1:], str(out+list(("".join(reversed(s1)))).pop() + list(("".join(reversed(s2)))).pop()))
    return helpLaceStrings(s1, s2, '')


def Square(x):
    return SquareHelper(abs(x), abs(x))
    

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x



            
