# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 10:42:52 2025

@author: HP
"""

# Input from user
n = int(input("Enter a number: "))
m = n

even_num = 0
odd_num = 0

# Loop through each digit
while n!=0:
    r = n % 10
    if r % 2 == 0:
        even_num += r
    else:
        odd_num += r
    n = n // 10

# Check condition
if even_num == odd_num:
    print(m, "is a Lead Number.")
else:
    print(m, "is NOT a Lead Number.")
