# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 08:38:51 2025

@author: HP
"""

def fibo(n):
    a=0
    b=1
    for i in range(n-1):
        print(a)
        c=a+b
        a=b
        b=c
    return a
n=int(input("enter the number:"))
f=fibo(n)
print(f)