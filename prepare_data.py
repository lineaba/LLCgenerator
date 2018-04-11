# -*- coding: utf-8 -*-
"""
PREPARE DATA FOR LLC NAMEGENERATOR
This program prepares data to be used for the LLC namegenerator. 
The wordcollection comes from XXXX
Only nouns, verbs and adjectives with initial letter "l" or "c" are selected, and written to two
seperate files (one for c words, and one for l words)
The output files contains one word on each line, followed by ; and then the part of speech tag v(verb), n(noun), a(adjective)

NOTE: the freq_dict file comes from here: https://www.wordfrequency.info/free.asp

Written by: Linea Brink Andersen
Date: april 10th 2018

"""

import pandas as pd

#read from the dictionary commaseperated file freq_dict
dictionary = pd.read_table("freq_dict.csv", ";")

#make a list of all the entries in the "word" column
word_list = list(dictionary["Word"])

#preprocess data by removing three-spaces which are present in the beginning of each word entry
#$$$inthewild1$$$#
for index, word in enumerate(word_list):
    word = word[3:]
    word_list[index] = word


#make a list of all the entries in the "word" column
part_of_speech = list(dictionary["Part of speech"])

#empty lists to hold the l-words and c-words
l_words = []
c_words = []

#update wordlist to only contain tupples of words and their part-of-speech tag
dictionary = zip(word_list, part_of_speech)

#go through dictionary, and pull words starting with L and C, and append them (and their PoS tag, to the two individual lists)
for element in dictionary:
    if element[0][0] == "l":
        l_words.append(element)
    if element[0][0] == "c":
        c_words.append(element)

#create new lists to contain only L and C words, respectively, that are nouns,verbs or adjectives 
l_noun_verb_adj = []
c_noun_verb_adj = []

#go through l list, and pull all l-words which are nouns, verbs and adjectives and append them (with their PoS tag to the new l-list)
for element in l_words:
    if element[1] == "v" or element[1] == "n" or element[1] == "a":
        l_noun_verb_adj.append(element)

#go through c list, and pull all c-words which are nouns, verbs and adjectives and append them (with their PoS tag to the new c-list)
for element in c_words:
    if element[1] == "v" or element[1] == "n" or element[1] == "a":
        c_noun_verb_adj.append(element)

#write the l-words and their PoS tags to the l_file
l_file = open("l_words.txt", "w")
for element in l_noun_verb_adj:
    print_this = element[0]+";"+element[1]
    l_file.write(print_this)
    l_file.write("\n")
l_file.close()

#write the c-words and their PoS tags to the l_file
c_file = open("c_words.txt", "w")
for element in c_noun_verb_adj:
    print_this = element[0]+";"+element[1]
    c_file.write(print_this)
    c_file.write("\n")
c_file.close()
