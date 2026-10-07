# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 19:17:22 2025

@author: HP
"""

def parameter(n):
    if(n%2==0):
        return True
    else:
        return False
n=int(input("enter number:"))
p=parameter(n)
print("Number is even",p)
