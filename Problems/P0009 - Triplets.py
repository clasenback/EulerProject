# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 18:20:48 2021

@author: User

SPECIAL PYTHAGOREAN TRIPLET

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

target = 1000
print("TARGET:", target)
a = 0
b = 1
control = True
triplet = [0, 0, 0]


while control:
    a += 1
    for m in range(a, target - a - b + 1):
        b = a + 1
        for n in range(b, target - a - b + 1):
            c = target - m - n
            if n > m and m**2 + n**2 == c**2:
                print("TRIPLET FOUND:", m, n, c)
                control = False
                triplet = m, n, c
    if a > target: control = False
    

print("CHECKING:")
print("A**2 + B**2 = C**2 CHECK")
print(triplet[0]**2, triplet[1]**2, triplet[0]**2 + triplet[1]**2, triplet[2]**2)
print("PRODUCT ABC:", triplet[0]*triplet[1]*triplet[2])
