# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:52:36 2021

@author: User

10001st PRIME

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

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

primos = [2]
ultimo = 10001
while len(primos) < ultimo:
    primos.append(nextPrime(primos[-1],primos))

print("O", ultimo,"º número primo é", primos[-1])
#print(primos)
print("A quantidade de primos descobertos é", len(primos))
    
