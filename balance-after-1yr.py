#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:24:49 2018

@author: vicky
"""
balance = 3870
principle = balance
annualInterestRate = .18
monthlyInterestRate = annualInterestRate/12
lowestpayment = round((balance/12),-1)

# how much do you need to pay each month to pay off entire debt load?

while balance > 0:
    balance = principle
    for month in range(1,13):
        balance = (balance - lowestpayment)*(1+monthlyInterestRate)
    lowestpayment += 10
        

print("Lowest payment: " + str(int(lowestpayment-10)))