# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:54:23 2021

@author: ALEX BACK

1000-DIGIT FIBONACCI NUMBER

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 
digits?
"""
# IMPORTING
from datetime import datetime as date 

# FUNCTIONS
def nextFibonacci(series):
    if len(series) < 2: series = [1, 1]
    return series[-1] + series[-2]

def numberOfDigits(n):
    return len(str(n))

# INITIALIZATION
target = 1000
fibonacci = [1, 1]
control = 1
start = date.now()

# PROCESSING
print("DIGITS, TIME")
while numberOfDigits(fibonacci[-1]) < target: 
    fibonacci.append(nextFibonacci(fibonacci))
    if len(fibonacci) >= control:
        control = control * 2
        print(numberOfDigits(fibonacci[-1]), date.now() - start)

# OUTPUT    
print("LENGTH, TIME")
print(len(fibonacci), date.now() - start)
# print(fibonacci[:5], fibonacci[-3], fibonacci[-2], fibonacci[-1])