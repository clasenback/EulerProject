# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:48:18 2021

@author: ALEX BACK

PANDIGITAL PRODUCTS

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.
"""
# IMPORTING
from datetime import datetime as date

# FUNCTIONS
def totalTime(t): 
    return date.now() - t

def permutationsOf(digits):
    if len(digits) == 0 : return []
    if len(digits) == 1 : return digits
    permutations = []
    for pos in range(len(digits)):
        for permutation in permutationsOf(digits[:pos] + digits[pos+1:]):
            permutations.append(digits[pos] + permutation)
    return permutations

def isPandigitalProduct(n):
    if int(n[:1]) * int(n[1:5]) == int(n[5:]): # 1d * 4d = 5d
        return (True, int(n[:1]), int(n[1:5]), int(n[5:]))
    if int(n[:2]) * int(n[2:5]) == int(n[5:]): # 2d * 3d = 5d
        return (True, int(n[:2]), int(n[2:5]), int(n[5:]))
    if int(n[:3]) * int(n[3:5]) == int(n[5:]): # 3d * 2d = 5d
        return (True, int(n[:3]), int(n[3:5]), int(n[5:]))
    if int(n[:4]) * int(n[4:5]) == int(n[5:]): # 4d * 1d = 5d
        return (True, int(n[:4]), int(n[4:5]), int(n[5:]))
    return (False,)

# INITIALIZING
t = date.now()
control = 2
panProducts = []
products = []
permutations = permutationsOf("123456789")
print(len(permutations), totalTime(t))

# PROCESSING
for permutation in permutations: 
    pandigital = isPandigitalProduct(permutation)
    if pandigital[0]: 
        panProducts.append(pandigital)
        print(panProducts[-1], totalTime(t))
        if pandigital[3] not in products:
            products.append(pandigital[3])


# OUTPUT
print(len(panProducts), sum(products), totalTime(t))