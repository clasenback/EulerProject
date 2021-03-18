# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 19:29:48 2021

@author: ALEX BACK

DIGIT FACTORIALS

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
# IMPORTING
from datetime import datetime as date 

# FUNCTIONS
def factorial(n):
    product = 1 
    for i in range(1, n+1) : product *= i
    return product

def factorials0_9To():
    factorials = {}
    for a in range(0,10):
        factorials[str(a)] = factorial(a)
    return factorials

def maxSumOfFactorialsOfDigits():
    digits = 1
    while True : 
        digits += 1
        if len(str(digits * (factorial(9)))) < digits : break
    return (digits-1) * factorial(9)

# INITIALIZATION
curiousNumbers = []
control = 2
start = date.now()
factorials = factorials0_9To()

# PROCESSING
for n in range(11, maxSumOfFactorialsOfDigits()+1): 
    summation = 0
    for digit in str(n):
        summation += factorials[digit]
    if summation == n :
        curiousNumbers.append(n)
    if len(curiousNumbers) == control :
        control *= 2
        print(len(curiousNumbers), date.now() - start)
# OUTPUT
print(len(curiousNumbers), date.now() - start)
print("A SOMA É", sum(curiousNumbers))