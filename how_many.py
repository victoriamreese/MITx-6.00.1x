#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 08:30:47 2018

@author: vicky
"""
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    counter = 0
    x = list(aDict.values())
    for i in x:
        if len(i) == 1:
            counter += 1
        elif len(i) > 1:
           for p in i:
               counter +=1
    print(counter)

how_many(animals)