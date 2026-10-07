# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 10:28:12 2025

@author: HP
"""

def file(file1,file2):
    f1=open(file1,"r")
    f2=open(file2,"w")
    f=1
    for i in f1:
        if(f%2==1):
            f2.write(i)
        f+=1
    f1.close()
    f2.close()
    print("odd line copied.")
    
file("file1.txt","file2.txt")
