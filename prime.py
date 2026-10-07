'''# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 20:00:46 2025

@author: HP
"""

n=int(input("Enter the number:"))
flag=1
if n==1:
    flag=0
for i in range(2,n//2+1):
    if(n%i==0):
        flag=0
        break
if(flag==1):
    print("prime")
else:
    print("not prime")
    '''
# prime
n=int(input("Enter the number:"))
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
if(flag==0):
    print("prime")
else:
    print("not prime")