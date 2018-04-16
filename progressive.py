# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 21:08:38 2018

@author: linea_000
"""
##PROBLEM: What happens (+should happen) if a word ending in cvc is not cmudict?

import nltk

def last_syllable_stressed(word):
    entries = nltk.corpus.cmudict.entries()
    for entry in entries:
        if entry[0] == word:
            stress_pattern = []
            for phone in entry[1]:
                for char in phone:
                    if char.isdigit():
                        char = int(char)
                        stress_pattern.append(char)              
    if stress_pattern[-1] != 0:
        return True
    else:
        return False

def progressive(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    if word[-2:] == "ie":
        word = word[:-2]
        word = "".join((word, "ying"))
    elif word[-1:] == "e":
        word = word[:-1]
        word = "".join((word, "ing"))
    elif (word[-3] not in vowels) and (word[-2] in vowels) and (word[-1] not in vowels):
        if last_syllable_stressed(word):
            word = "".join((word, word[-1], "ing"))
        else:
            word = "".join((word, "ing"))
    else:
        word = "".join((word, "ing"))
    return word

l_words = open("l_words.txt", "r")
l_verbs = []
for line in l_words:
    if line[-2] == "v":
        verb = line[:-3]
        verb_prog = progressive(verb)
        l_verbs.append((verb, verb_prog))
l_words.close()

l_progs = open("l_progs.txt", "w")
for tup in l_verbs:
    line = "".join((tup[0], ";", tup[1], "\n"))
    l_progs.write(line)
l_progs.close()

        