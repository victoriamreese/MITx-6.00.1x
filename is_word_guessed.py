#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:38:51 2018

@author: vicky
"""

secretWord = 'apple' 
lettersGuessed = ['a', 'e', 'p', 'q']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    word_set = set(secretWord)
    guessed_set = set(lettersGuessed)
    if word_set.issubset(guessed_set):
        return True
    else:
        return False
    
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word_set = set(secretWord)
    guessed_set = set(lettersGuessed)
    guessed_string = ""
    for i in secretWord:
        if i in guessed_set:
            guessed_string += " " + str(i) + " "
        elif i == " ":
            guessed_string += " / "
        elif i not in guessed_set:
           guessed_string += " _ "
    print(guessed_string)





def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    remaining_letters = ''
    guessed_set = set(lettersGuessed)
    for l in string.ascii_lowercase:
        if l not in guessed_set:
            remaining_letters += l
        else: 
            remaining_letters += ''
    return remaining_letters
    
getAvailableLetters(lettersGuessed)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    import string
    
    #instantiate game lists
    lettersGuessed = ''
    mistakesMade = ''
    
    #initiate game
    print('Hello and welcome to hangman!')
    
    #game proceeds as long as all letters in word are not guessed
    while not isWordGuessed(secretWord, lettersGuessed):
        print('there are ' + str(len(secretWord)) + ' letters in the secret word')
        letters = getAvailableLetters(lettersGuessed)
        print('you can guess: ' + str(letters) + '. Do not guess ' + str(mistakesMade))
        guess = input('what is your guess? (enter one letter): ')
        guess = str(guess.lower())
        
        
        #handles valid lowercase ascii guesses
        if guess in string.ascii_lowercase:
            #letters that haven't been guessed before
            if guess not in lettersGuessed:
                lettersGuessed += guess
                if guess in set(secretWord):
                    print('nice! you got one')
                    result1 = getGuessedWord(secretWord, lettersGuessed)
                    print(result1)
                else:
                    mistakesMade += guess
                    print('sorry that is not in the word')
                    result2 = getGuessedWord(secretWord, lettersGuessed)
                    print(result2)
                
            #letters that have been guessed before.
            else:
                print('you already guessed that!')
        
        #handles invalid guesses
        else:
            print('please enter a valid guess')
    
    #winning!
    else:
        print('congratulations, you won!')
        print(secretWord)
    
hangman("pineapple")