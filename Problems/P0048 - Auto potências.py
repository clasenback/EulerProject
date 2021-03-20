# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:52:58 2021

@author: ALEX BACK

SELF POWERS

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""
# IMPORTING
from datetime import datetime as date 

# FUNCTIONS

# INITIALISATION
target = 1000
summation = 0
start = date.now()
control = 2

# PROCESSING
for n in range(1, target+1): 
    summation += n ** n
    if n == control : 
        control *= 2
        print(n, date.now()-start)

# OUTPUT    
print(str(summation)[-10:], date.now()-start)