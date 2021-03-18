# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:44:36 2021

@author: User

SUM SQUARE DIFFERENCE

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10) ** 2 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.

"""
soma = 0
somaQuadrados = 0

for i in range(100+1):
    soma += i
    somaQuadrados += i**2
    
print(soma**2 - somaQuadrados)
    

