#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:59:34 2018

@author: vicky
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    us_num = str(us_num)
    if len(us_num) < 2:
        mand_num = trans[us_num]
    else:
        mand_num = ''
        first_num = us_num[0]
        second_num = us_num[1]
        if first_num == '1':
            mand_num += trans['10']
            mand_num += ' '
        if int(first_num) > 1:
            mand_num += trans[first_num] + ' '
            mand_num += trans['10'] + ' '
        if int(second_num) > 0: 
            mand_num += trans[second_num]
    print(mand_num)
    
        
    
# getting 8/10 - more testing required
    
    
    
def primes_list(N):
        primes = []
        for n in range(2, N+1):
            count = 0
            for i in range(2, n):
                if (n%i) == 0:
                    count+=1
                else: 
                    continue
            if count == 0:
                primes.append(n)
        print(primes)
                
    

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    uniques = []
    for key in aDict.keys():
        test_dict = aDict.copy()
        del test_dict[key]
        val_set = set(test_dict.values())
        if aDict[key] not in val_set:
            uniques.append(key)
    print(uniques)
    
#partially correct(16/20)- required testing
    
    
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'It is obvious that ' + Professor.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff 
    
    


class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    
    
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            pass

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if self.vals[e] != 0:
            return self.vals[e]
        else:
            return None