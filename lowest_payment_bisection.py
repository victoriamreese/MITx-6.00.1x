#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 23:32:32 2018

@author: vicky
"""

balance = 3870
annualInterestRate = .18
principle = balance
monthlyInterestRate = annualInterestRate/12
UB = (balance * (1+annualInterestRate)) / 12
LB = balance/12

guess = (UB + LB)/2
print(guess)
# how much do you need to pay each month to pay off entire debt load?

while round(balance, 1) != 0:
    balance = principle
    for month in range(1,13):
        balance = (balance - guess)*(1+monthlyInterestRate)
    print("remaining balance is: " + str(balance))
    if balance > 0:
        LB = guess
        guess = (UB + guess)/2
        print("Guess too low, new guess is: " + str(guess))
        
    elif balance < 0:
        UB = guess
        guess = (guess + LB)/2
        print("Guess too high, new guess is: " + str(guess))
    print("low bound: " + str(LB))
    print("high bound: " + str(UB))

        
if round(balance, 1)  == 0:
    print("Lowest payment: " + str(round(guess, 2)))