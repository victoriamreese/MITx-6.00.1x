#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 12:43:47 2018

@author: vicky
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    t = ()
    for i, a in enumerate(aTup):
        print(i)
        if i%2==0:
            t = t + (a,)
    print(t)

oddTuples((1, 2, 4, ('hellol', 3, True), 4, 'zambohi'))
