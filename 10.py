# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:02:35 2019

@author: Administrator
"""

num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial:",fact)