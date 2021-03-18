# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:20:38 2021

@author: User

If we list all the natural numbers below 10 that 
are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 
1000.
"""
def isMultipleOf(n,m):
    return n % m == 0 

sum = 0

for i in range(1000): 
    if isMultipleOf(i,3) or isMultipleOf(i,5): 
        sum += i

print (sum)
        
        