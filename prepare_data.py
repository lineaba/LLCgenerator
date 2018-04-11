# -*- coding: utf-8 -*-
"""
PREPARE DATA FOR LLC NAMEGENERATOR
This program prepares data to be used for the LLC namegenerator. 
The wordcollection comes from XXXX
Only nouns, verbs and adjectives with initial letter "l" or "c" are selected, and written to two
seperate files (one for c words, and one for l words)
The output files contains one word on each line, followed by ; and then the part of speech tag v(verb), n(noun), a(adjective)

Written by: Linea Brink Andersen
Date: april 10th 2018
"""

import pandas as pd

dictionary = pd.read_table("freq_dict.csv", ";")

word_list = list(dictionary["Word"])

for index, word in enumerate(word_list):
    word = word[3:]
    word_list[index] = word

part_of_speech = list(dictionary["Part of speech"])

l_words = []
c_words = []

dictionary = zip(word_list, part_of_speech)


for element in dictionary:
    if element[0][0] == "l":
        l_words.append(element)
    if element[0][0] == "c":
        c_words.append(element)

l_noun_verb_adj = []
c_noun_verb_adj = []

for element in l_words:
    if element[1] == "v" or element[1] == "n" or element[1] == "a":
        l_noun_verb_adj.append(element)

for element in c_words:
    if element[1] == "v" or element[1] == "n" or element[1] == "a":
        c_noun_verb_adj.append(element)

l_file = open("l_words.txt", "w")
for element in l_noun_verb_adj:
    print_this = element[0]+";"+element[1]
    l_file.write(print_this)
    l_file.write("\n")
l_file.close()

c_file = open("c_words.txt", "w")
for element in c_noun_verb_adj:
    print_this = element[0]+";"+element[1]
    c_file.write(print_this)
    c_file.write("\n")
c_file.close()
