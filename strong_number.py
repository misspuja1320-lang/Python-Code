# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 10:38:42 2025

@author: HP
"""

n = int(input("Enter number: "))
m = n
s = 0

while n != 0:
    r = n % 10
    n = n // 10
    # Correct factorial calculation
    f = 1
    for i in range(1, r + 1):  # Include r in the range
        f *= i
    
    s += f
    

# Check if strong number
if s == m:
    print("Strong")
else:
    print("Not Strong")
