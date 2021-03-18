# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:01:59 2021

@author: ALEX BACK

NUMBER LETTER COUNTS

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with 
British usage.
"""

# FUNCIONS 

def numeralsInEnglish(n):
    if n == 0 : return ""
    elif n == 1 : return "one"
    elif n == 2 : return "two"
    elif n == 3 : return "three"
    elif n == 4 : return "four"
    elif n == 5 : return "five"
    elif n == 6 : return "six"
    elif n == 7 : return "seven"
    elif n == 8 : return "eight"
    elif n == 9 : return "nine"
    
def decimalsInEnglish(n):
    rest = n % 10
    n = n // 10
    if n == 0 : return "" + numeralsInEnglish(rest)
    elif n == 1 : 
        if 10 * n + rest == 10 : return "ten"
        elif 10 * n + rest == 11 : return "eleven"
        elif 10 * n + rest == 12 : return "twelve"
        elif 10 * n + rest == 13 : return "thirteen"
        elif 10 * n + rest == 14 : return "fourteen"
        elif 10 * n + rest == 15 : return "fifteen"
        elif 10 * n + rest == 16 : return "sixteen"
        elif 10 * n + rest == 17 : return "seventeen"
        elif 10 * n + rest == 18 : return "eighteen"
        elif 10 * n + rest == 19 : return "nineteen"
    elif n == 2 : return "twenty " + numeralsInEnglish(rest)
    elif n == 3 : return "thirty " + numeralsInEnglish(rest)
    elif n == 4 : return "forty " + numeralsInEnglish(rest)
    elif n == 5 : return "fifty"  + numeralsInEnglish(rest)
    elif n == 6 : return "sixty " + numeralsInEnglish(rest)
    elif n == 7 : return "seventy " + numeralsInEnglish(rest)
    elif n == 8 : return "eighty " + numeralsInEnglish(rest)
    elif n == 9 : return "ninety"  + numeralsInEnglish(rest)
    
def hundredsInEnglish(n):
    rest = n % 100
    n = n // 100
    if n == 0 : return "" + decimalsInEnglish(rest)
    elif n > 0 and rest == 0 : return numeralsInEnglish(n) + " hundred" 
    elif n > 0 and rest > 0 : return numeralsInEnglish(n) + " hundred and " + decimalsInEnglish(rest)

def thousandsInEnglish(n):
    rest = n % 1000
    n = n // 1000
    if n == 0 : return "" + hundredsInEnglish(rest)
    else : return numeralsInEnglish(n) + " thousand " + hundredsInEnglish(rest)
    

palavra = ""
for i in range(1,1000+1):
    palavra += thousandsInEnglish(i).replace(" ","")
print(thousandsInEnglish(i))
print(len(palavra))