#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 07:59:11 2018

@author: vicky
"""

def count_smileys(arr):
    count = 0
    for smiley in arr:
        if smiley[int(len(smiley)-1)] == "D" or smiley[int(len(smiley)-1)] == ")":
            if smiley[0] == ":" or smiley[0] ==";":
                if smiley[1:int(len(smiley)-1)] == "-" or smiley[1:int(len(smiley)-1)] == "~" or smiley[1:int(len(smiley)-1)] == "":
                    count +=1
                else: 
                    count += 0
            else: 
                count += 0
        else:
            count +=0
    return count

    
def filter_list(l):
    return [i for i in l if type(i)==int]

ar
def square_digits(num):
    squared = ([int(i)**2 for i in str(num)])
    #final = ''.join(squared)
   # print(final)
    


def longest_consec(strarr, n):
    longest= ''
    for i, k in enumerate(strarr):
        new = ''.join(strarr[i:n+i])
        if len(longest) < len(new):
            longest = new
                      
    print(longest)
    return longest


#def goodVsEvil(good, evil):
    