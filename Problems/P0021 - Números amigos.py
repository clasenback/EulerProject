# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:47:17 2021

@author: ALEX BACK

AMICABLE NUMBERS

Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; 
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
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

# INPUTS
target = 10000
amicables = []
summation = 0
start = date.now()

# PROCESSING
for n in range(2,target+1) :
    somaFatoresN = sum(listFactors(n))
    if somaFatoresN > n: 
        somaFatoresM = sum(listFactors(somaFatoresN))
        if somaFatoresM == n : 
            amicables.append([n, somaFatoresN])
            print(amicables[-1], "in", date.now() - start)
for pairs in amicables: 
    summation += sum(pairs)

# OUTPUT
print("THE SUM OF ALL AMICABLE NUMBERS UNDER", target, "IS", summation, "in", 
      date.now() - start)