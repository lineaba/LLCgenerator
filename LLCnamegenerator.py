# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 13:06:37 2018

@author: linea_000
"""

'''
This is the LLC-name generater
'''


import pandas as pd
import random


#prepare data
l_file = open("l_words.txt", "r")
l_dict = []
for line in l_file:
    element = line.split(";")
    tup = (element[0], element[1][0])
    l_dict.append(tup)
l_file.close()
l_dict = dict(l_dict)

c_file = open("c_words.txt", "r")
c_dict = []
for line in c_file:
    element = line.split(";")
    tup = (element[0], element[1][0])
    c_dict.append(tup)
c_file.close()
c_dict = dict(c_dict)

word_patterns


'''
###FROM HERE HAVE NOT WORKED
#gotta make a list of keys, in order to pick a random number from there

l_words = l_dict.keys()
c_words = c_dict.keys()



###I AM NOT CURRENTLY ENSURING THAT WORDS ARE NOT SAME
def select_lwords():    
    word1 = l_words[random.randint(0, len(l_words)-1)]
    word2 = l_words[random.randint(0, len(l_words)-1)]
    return word1, word2
    #am I gonna need to return the tup?
  
word3 = c_words[random.randint(0, len(c_words))]

counter = 1
for i in range(10000):
    tup = select_lwords()
    if tup[0] == tup[1]:
        print "OOOPS"
        counter += 1
print "DONE"
print counter

print tup

#print word1, word2, word3
'''