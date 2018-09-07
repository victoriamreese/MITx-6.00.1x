#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 20:03:05 2018

@author: vicky
"""

#Initiation variables


high = 100
low = 0
guess = (high + low)//2.0

print("Please think of a number between 0 and 100!")
import time; time.sleep(1)

#starting guess & feed back (50, low or high)
print("Is your secret number " + str(int(guess)) + '?')
response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while response != 'c': 
#for low guesses
    if response == 'l':
        low = guess
        guess= (guess + high)//2.0

# for high guesses
    elif response == 'h':
        high = guess
        guess = round(low + guess)//2.0
        
    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(int(guess)) + '?')
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

        break
    print("Is your secret number " + str(int(guess)) + '?')
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")


if response == 'c':
    print("Game over. Your secret number was: " + str(int(guess)))
    
