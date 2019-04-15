# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:53:31 2019

@author: Administrator
"""

num=int(input("Enter a number:"))
rev=0
while(num>0):
    div=num%10
    rev=(rev*10)+div
    num=num//10
print("Reverse Number=",rev)