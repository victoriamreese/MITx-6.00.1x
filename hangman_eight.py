#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 22:23:59 2018

@author: vicky
"""
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
    return guessed_string

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
    i = 8
    
    #initiate game
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    #game proceeds for 8 tries
    while i > 0:
        print('-----------')
        print('You have ' + str(i) + ' guesses left.')
        letters = getAvailableLetters(lettersGuessed)
        print('Available letters: ' + str(letters))
        guess = input('Please guess a letter: ')
        guess = str(guess.lower())
        
        
        #handles valid lowercase ascii guesses
        if guess in string.ascii_lowercase:
            
            #letters that haven't been guessed before
            if guess not in lettersGuessed:
                
                lettersGuessed += guess
                if guess in set(secretWord):
                    i-=1
                    print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                    
                    if isWordGuessed(secretWord, lettersGuessed):
                        break
                else:
                    mistakesMade += guess
                    i -= 1
                    print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))

            #letters that have been guessed before.
            else:
                print('Oops! You\'ve already guessed that letter: ' + str(getGuessedWord(secretWord, lettersGuessed)))

                
        #handles invalid guesses
        else:
            return 'Please enter a valid guess.'
    
    #losing
    else:
        print('-----------')
        print('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')
    

    if isWordGuessed(secretWord, lettersGuessed):
        print('-----------')
        print('Congratulations, you won!')
    
    
hangman('quirk')
