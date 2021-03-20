# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:13:32 2021

@author: ALEX BACK

TRIANGULAR, PENTAGONAL AND HEXAGONAL

Triangle, pentagonal, and hexagonal numbers are generated by the following 
formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

"""
# IMPORTING
from datetime import datetime as date 

# FUNCTIONS
def triangleOf(n):
    return n * (n+1) / 2

def pentagonalOf(n):
    return n * (3 * n - 1) / 2

def hexagonalOf(n):
    return n * (2 * n - 1)

# INITIALIZATION
triangles = []
pentagonals = []
hexagonals = []
curious = []
target = 3
n = 1
control = 2
start = date.now()

# PROCESSING
while True:
    hexagonals.append(hexagonalOf(n))
    pentagonals.append(pentagonalOf(n))
    triangles.append(triangleOf(n))
    if triangles[-1] in pentagonals and triangles[-1] in hexagonals:
        curious.append(triangles[-1])
    if n == control: 
        print(control, date.now() - start)
        control *= 2
    if len(curious) == target : break
    n += 1
        
# OUTUPUT
print(n, curious, "IN", date.now() - start)