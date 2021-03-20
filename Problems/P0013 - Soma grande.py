# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:29:43 2021

@author: ALEX BACK

LARGE SUM

Work out the first ten digits of the sum of the following one-hundred 50-digit 
numbers.
"""
# IMPORTING
import csv

# FUNCTIONS

# INITIZALIZATION
path = "C:/Users/User/Documents/AA - Pessoal/DataScience/Project Euler/"
file = "p013_numbers.txt"
numbers = []

# PROCESSING
with open(path + file) as arquivo:
    content = csv.reader(arquivo)
    for row in content: 
        numbers.append(int(row[0]))

# OUTPUT
print(len(numbers))        
print(str(sum(numbers))[:10])