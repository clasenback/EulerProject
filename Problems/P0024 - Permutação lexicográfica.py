# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:18:00 2021

@author: ALEX BACK

LEXICOGRAPHIC PERMUTATIONS

A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
]are listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def permutationsOf(digits):
    if len(digits) == 0 : return []
    if len(digits) == 1 : return digits
    permutations = []
    for pos in range(len(digits)):
        for permutation in permutationsOf(digits[:pos] + digits[pos+1:]):
            permutations.append(digits[pos] + permutation)
    return permutations

permutations = permutationsOf("0123456789")
print(permutations[1000000-1])