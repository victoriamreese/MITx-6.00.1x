#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:43:43 2018

@author: vicky
"""


def persistance(num):
    count = 0
    product = 1
    while len(str(num)) != 1:
        for i in str(num):
            product *= int(i) 
        count += 1
        num = product
        product =1
        print(num)
        print("the count is: " + str(count))   
    return count
    
persistance(39)