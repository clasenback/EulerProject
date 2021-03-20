# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:55:41 2021

@author: ALEX BACK

NAMES SCORE

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name 
score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN 
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

# IMPORTING
import csv

# FUNCTIONS
def nameScore(name):
    ALPHABET = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")    
    score = 0
    for letter in name:
        score += ALPHABET.index(letter) + 1
    return score

# INITIZALIZATION

path = "C:/Users/User/Documents/AA - Pessoal/DataScience/Project Euler/"
file = "p022_names.txt"
names = []
scores = []

# PROCESSING
with open(path + file) as arquivo:
    content = csv.reader(arquivo, delimiter=',')
    for row in content: 
        for name in row: 
            names.append(name)
names.sort()
for name in range(len(names)): 
    scores.append((name + 1) * nameScore(names[name]))
            
# OUTPUT
print(len(scores), sum(scores))
