# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:10:13 2021

@author: ALEX BACK

lARGEST PALINDROME PRODUCT

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Exemplos:
https://www.w3schools.com/python/python_howto_reverse_string.asp

"""

def isPalindrome(n):
    # slicing
    return int(str(n)[::-1]) == n

# definição variáveis iniciais
palindromos = []
candidatos = []

# encontra todos os candidatos 
for n in range(999,100,-1):
    for m in range(999,100,-1):
        if n >= m:
            candidatos.append(n*m)

# encontra os palindromos entre os candidatos
for n in candidatos:
    if isPalindrome(n):
        palindromos.append(n)

# apresenta os resultados
print("O tamanho da lista de candidatos é", len(candidatos))
print("O maior candidato é", max(candidatos))
print("O tamanho da lista de palindromos é", len(palindromos))
print("O maior palindromo é", max(palindromos))  