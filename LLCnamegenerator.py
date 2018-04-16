# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 13:06:37 2018

@author: linea_000
"""

'''
This is the LLC-name generater
'''
#PROBLEM: not currently ensuring that there is no repeat word in LLC
#need to incorporate -ing form of verbs, or a set of rules for how to construct -ing words correct

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

def prepare_dict(file_name):
    open_file = open(file_name, "r")
    dictionary = []
    for line in open_file:
        if line[-1] == "\n":
            line = line[:-1]
        element = line.split(";")
        dictionary.append((element[0], element[1]))
    open_file.close()
    dictionary = dict(dictionary)
    return dictionary
    

##invert dictionary function
def invert_dict(dictionary):
    wordclass_dict = {}
    for k, v in dictionary.iteritems():
        wordclass_dict.setdefault(v, []).append(k)
    return wordclass_dict

wordclass_ldict = invert_dict(l_dict)
wordclass_cdict = invert_dict(c_dict)

def adj_adj_noun():
    l_adj = wordclass_ldict["j"]
    c_noun = wordclass_cdict["n"]
    word1 = l_adj[random.randint(0, len(l_adj)-1)]
    word2 = l_adj[random.randint(0, len(l_adj)-1)]
    word3 = c_noun[random.randint(0, len(c_noun)-1)]
    return word1+" "+word2+" "+word3

def adj_verbing_noun():
    l_adj = wordclass_ldict["j"]
    l_verb = wordclass_ldict["v"]
    c_noun = wordclass_cdict["n"]
    l_progs = prepare_dict("l_progs.txt")
    word1 = l_adj[random.randint(0, len(l_adj)-1)]
    word2 = l_verb[random.randint(0, len(l_verb)-1)]
    word2 = l_progs[word2]
    word3 = c_noun[random.randint(0, len(c_noun)-1)]
    return word1+" "+word2+" "+word3
    
def adj_noun_noun():
    l_adj = wordclass_ldict["j"]
    l_noun = wordclass_ldict["n"]
    c_noun = wordclass_cdict["n"]
    word1 = l_adj[random.randint(0, len(l_adj)-1)]
    word2 = l_noun[random.randint(0, len(l_noun)-1)]
    word3 = c_noun[random.randint(0, len(c_noun)-1)]
    return word1+" "+word2+" "+word3

def make_name():
    pattern = random.randint(0, 2)
    if pattern == 0:
        print "1"
        LLC = adj_adj_noun()
    elif pattern == 1:
        print "2"
        LLC = adj_verbing_noun()
    elif pattern == 2:
        print "3"
        LLC = adj_noun_noun()
    else:
        print "SOMETHING WENT TERRIBLY WRONG"
        LLC = ""
    return LLC
        
        
print make_name()
    
'''
if pattern == 0:
    LLC = aan()
elif pattern == 1:
    LLC = abv()
elif pattern == 2:
    LLC = ann()

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