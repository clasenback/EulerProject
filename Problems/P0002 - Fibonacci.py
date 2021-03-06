# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:42:29 2021

@author: User

Each new term in the Fibonacci sequence is 
generated by adding the previous two terms. By 
starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, find the 
sum of the even-valued terms.

"""

def fibonacciAte(n):
    nMenosDois = 0
    nMenosUm = 1
    somaAnteriores = 0
    result = []
    while somaAnteriores <= n:
        somaAnteriores = nMenosDois + nMenosUm 
        result.append(somaAnteriores)
        (nMenosDois, nMenosUm) = (nMenosUm, somaAnteriores)
    result.pop()
    return result

def somarPares(lista):
    soma = 0
    for elemento in lista:
        if elemento % 2 == 0: 
            soma += elemento
    return soma

n = fibonacciAte(4000000)
print(n)
print(somarPares(n))

