# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:06:22 2019

@author: Administrator
"""

n=int(input("Enter range:"))
for i in range(1,n):
    if(i%3==0 and i%5==0):
        print(i,"= fizzbuzz")
    elif(i%3==0):
        print(i,"=Red")
    elif(i%5==0):
        print(i,"= Black")