#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:03:35 2018

@author: vicky
"""

s = "qxumseqjpvx"
substring = ''
longest = ''  
for i in range(0, len(s)-1):
    if not substring:
        substring = s[i]
    if s[i] < s[i+1] or s[i] == s[i+1]:
        substring += str(s[i+1])
    else:
        if len(longest) < len(substring):
            longest = substring
        substring = ''
    print(substring)
    print(i)
    print(longest)
    print(len(s))
    if i == len(s)-2 and len(substring) > len(longest):
        longest = substring
        break

print("Longest substring in alphabetical order is: " + str(longest))