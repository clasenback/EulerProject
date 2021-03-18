# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:40:21 2021

@author: User

FACTORIAL DIGIT SUM

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

#IMPORTING
from datetime import datetime as date 

def digitSum(n):
    summation = 0
    for i in str(n): summation += int(i)
    return summation

def factorial(n):
    product = 1 
    for i in range(1, n+1) : product *= i
    return product

print(digitSum(factorial(100)))