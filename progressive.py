# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 21:08:38 2018

@author: linea_000
"""
#if last syllable is stressed, and have structure cvc, repeat last consonant, before adding ing
#I think best solution here will be to use the pronounciation dictionary from NLTK, to find stress patterns - however, need to deal if words are not in dictionary?!

def progressive(word):
    #gotta handle the fact that the word could be so short that you can't take that much of a substring!
    if word[-2:] == "ie":
        word = word[:-2]
        word = "".join((word, "ying"))
    elif word[-1:] == "e":
        word = word[:-1]
        word = "".join((word, "ing"))
    #elif last three letters are consonant, vowel, consonant
        #if the last syllable is stressed (and possibly that itr includes the CVC)
            #repeat last consonant, before adding "ing"
    else:
        word = "".join((word, "ing"))
    return word

print progressive("smile")