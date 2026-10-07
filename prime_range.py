# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 20:07:26 2025

@author: HP
"""

n=int(input("Enter the number:"))
for i in range(2,n+1):
    for j in range(2,i+1):
        if(i%j==0):
            break
    if(i==j):
        print(i,"prime")