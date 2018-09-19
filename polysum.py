#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:43:44 2018

@author: vicky
"""

import math 

def polysum(n, s):
    '''
    n: integer, number of sides 
    s: float or integer, length of sides of regular polynomial
    returns: sum of the area and square of the perimeter of the polynomial. 
    '''
    #area calculation
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    
    #perimeter squared calculation
    perimeter_squared = (s*n)**2
    
    
    #add area and perimeter, round to 4 decimals.
    result = round(area+perimeter_squared, 4)
    
    return result