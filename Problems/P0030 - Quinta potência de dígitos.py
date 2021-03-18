# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:35:23 2021

@author: ALEX BACK

DIGIT FIFTH POWERS

Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.

"""

# FUNCTIONS
def powers0_9To(n):
    powers = {}
    for a in range(0,10):
        powers[str(a)] = a ** n
    return powers

def maxSumOfPowersOfDigits(power):
    digits = 1
    while True : 
        digits += 1
        if len(str(digits * (9 ** power))) < digits : break
    return (digits-1) * (9 ** power)

# INITIALIZATION
power = 5
powers = powers0_9To(power)
coincidences = []

# PROCESSING
for n in range(11, maxSumOfPowersOfDigits(power)+1): 
    summation = 0
    for digit in str(n):
        summation += powers[digit]
    if summation == n :
        coincidences.append(n)
        
# OUTPUT
print(sum(coincidences))