# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:43:35 2021

@author: ALEX BACK

In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
# IMPORTING
import math
from datetime import datetime as date 

# FUNCTIONS
def coinsProduct(coins, coinValues):
    summation = 0
    for coin in range(len(coins)): summation += coins[coin] * coinValues[coin]
    return summation

def changePermutationsFor(amount, coinValues):
    if len(coinValues) == 0 : return []
    permutations = []
    for qty in range(1 + math.ceil(amount/coinValues[0])):
        change = amount - qty * coinValues[0]
        if change == 0 : 
            permutations.append([qty] + [0] * len(coinValues[1:]))
            continue
        for permutation in changePermutationsFor(change, coinValues[1:]):
            permutations.append([qty] + permutation)
    return permutations

# INITIALIZATION
coinValues = [200, 100, 50, 20, 10, 5, 2, 1]
amount = 200
t = date.now()
print("Troco para", amount, "com as moedas", coinValues)

# PROCESSING
permutations = changePermutationsFor(amount, coinValues)

# OUTPUT
print(len(permutations), "different ways. In", date.now()-t)
