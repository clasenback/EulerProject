# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:56:02 2021

@author: ALEX BACK

SMALLEST MULTIPLE

2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
"""

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

def primesUntil(n):
    primes = [2]
    i = 2
    while i < n:
        if nextPrime(i, primes) <= n:
            primes.append(nextPrime(i, primes))
        if i == primes[-1]:
            i = i + 1 
        else:
            i = primes[-1]
    return primes

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

def allPrimeFactorsInRange(n):
    fatores = {}
    for i in range(2, n+1):
        fatores[i] = primeFactors(i)
    return fatores

def allPrimeFactorsUntil(n):
    primos = primesUntil(n)
    todosFatores = allPrimeFactorsInRange(n).values()
    n_primos = {}
    saida = []
    for primo in primos:
        for lista in todosFatores:
            saida.append(lista.count(primo))
        n_primos[primo] = max(saida)
        saida = []
    return n_primos
    
"""
print(primesUntil(20))
print(allPrimeFactorsInRange(20))
"""
print(allPrimeFactorsUntil(20))

ocorrencias = allPrimeFactorsUntil(20)
result = 1 
for primo in ocorrencias: 
    print(primo, "elevado a", ocorrencias[primo], "é igual a", primo ** ocorrencias[primo])
    result = result * primo ** ocorrencias[primo]
    
print("O produto destas potências é", result)

