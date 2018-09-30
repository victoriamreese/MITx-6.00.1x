#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 09:35:47 2018

@author: vicky
"""
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    numbers.reverse()
    two_smallest = numbers.pop()
    two_smallest += numbers.pop()
    return two_smallest

