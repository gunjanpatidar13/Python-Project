# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:25:44 2019

@author: Administrator
"""

l=input("Enter elements of list:").split()
print("Original List=",l)
r=l[::-1]
print("Reversed List=",r)
sum=[]
for i in range(0,len(l)):
    s=int(l[i])+int(r[i])
    sum.append(s)
print("Sum=",sum)