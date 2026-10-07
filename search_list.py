# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 18:45:34 2025

@author: HP
"""

n=int(input("Enter the number"))
l=[]
for i in range(1,n+1):
    l.append(i)
print("L=",l)
sn=int(input("Enter searching item:"))
f=0
for i in l:
    if(i==sn):
        f=1
        break
if(f==1):
    print(sn,"is found")
else:
    print(sn,"is not found")