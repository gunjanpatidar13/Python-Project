# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:43:11 2019

@author: Administrator
"""

num=int(input("Enter a number:"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1

if(flag==0):
    print("Prime Number")
else:
    print(" Not Prime Number")
    