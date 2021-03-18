# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 10:44:22 2021

@author: ALEX BACK

POWER DIGIT SUM

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""
#IMPORTING
from datetime import datetime as date 

def digitSum(n):
    summation = 0
    for i in str(n): summation += int(i)
    return summation

print(date.now())
print(digitSum(2**1000))
print(date.now())