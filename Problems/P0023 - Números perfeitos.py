# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:53:01 2021

@author: ALEX BACK

A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 28 
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than 
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers is 
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers.
"""
# IMPORTING
from datetime import datetime as date

# FUNCTIONS
def nextPrime(n, primos):
    if n % 2 == 0: 
        n +=1
    isPrime = False
    while not isPrime:
        for primo in primos:
            if n % primo == 0:
                n +=2
                break
            if primo == primos[-1]:
                isPrime = not isPrime
    return n

def firstPrimeFactor(n):
    primos = [2]
    fatores = []
    if n == 1 : 
        return 1        
    while n > 1:
        if n % primos[-1] == 0: 
            n = n / primos[-1]
            fatores.append(primos[-1])
            break
        else: 
            primos.append(nextPrime(primos[-1], primos))
    return fatores[0]

def listFactors(n):
    factors = [1]
    if n % 2 == 0: 
        prime = 2
        step = 1
    else : 
        prime = firstPrimeFactor(n)
        step = 2
    for i in range(prime ,1+n//prime, step):
        if n % i == 0: 
            factors.append(i)
    return factors

def isAbundant(n, factors):
    return sum(factors) > n

def isSumOfTwoAbundants(n, knownAbundants):
    for abundant in knownAbundants: 
        if (n - abundant <= abundant) and (n - abundant in knownAbundants) : 
            return True
    return False

# INITIALIZATION
control = 1000
target = 28123 #28123
knownAbundants = []
sumOfTwoAbundants = []
notSumOfTwoAbundants = [1, 2]
start_time = date.now()

# PROCESSING
for n in range(3, target+1): 
# finding all abundants until target
    if isAbundant(n, listFactors(n)): 
        knownAbundants.append(n)
        if len(knownAbundants) > control:
            print(n, len(knownAbundants), date.now() - start_time)
            control += 1000
    if len(knownAbundants) == 0 : 
        notSumOfTwoAbundants.append(n)
        continue
# finding all numbers that are or are NOT a sum of two abundants
    if not isSumOfTwoAbundants(n, knownAbundants):
        notSumOfTwoAbundants.append(n)
    else: 
        sumOfTwoAbundants.append(n)

# OUTPUT
print("THE SUM IS", sum(notSumOfTwoAbundants), "IN", date.now() - start_time)