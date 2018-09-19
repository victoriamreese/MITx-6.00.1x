#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:25:31 2018

@author: vicky
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    x = list(aDict.values())
    if len(x) == 0:
        return None
    longest = len(x[0])
    for i, n in enumerate(x):
        if longest < len(x[i]):
            longest = len(x[i])
    return 'b'
       
    
        
biggest(animals)
    