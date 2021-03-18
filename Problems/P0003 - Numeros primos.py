# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:00:03 2021

@author: User

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def isPrime(n):
    result = True
    for i in range(2, n, 1): 
        if n % i == 0 : 
            result = False
    return result 

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

def primeFactors(n):
    primos = [2]
    fatores = []
    while n > 1:
        if n % primos[-1] == 0: 
            n = n / primos[-1]
            fatores.append(primos[-1])
        else: 
            primos.append(nextPrime(primos[-1], primos))
    return fatores

n = 600851475143 
print("O maior fator primo de", n, "é", primeFactors(n)[-1])