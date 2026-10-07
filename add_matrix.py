# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 00:15:08 2025

@author: HP
"""

r1=int(input("Enter the first row number:"))
c1=int(input("Enter the first column number:"))
r2=int(input("enter the second row number:"))
c2=int(input("Enter the second column number:"))

print("Enter the first matrix")
a=[]
for i in range(r1):
    r=[]
    for j in range(c1):
        val=int(input("Enter the values:"))
        r.append(val)
    a.append(r)
    
print("Enter the second matrix")
b=[]
for i in range(r2):
    r=[]
    for j in range(c2):
        val=int(input("Enter the values:"))
        r.append(val)
    b.append(r)
    
result=[]
for i in range(r1):
    r=[]
    for j in range(c2):
        c=a[i][j]+b[i][j]
        r.append(c)
    result.append(r)
    
print("Result matrix addition:")
for r in result:
    print(r)