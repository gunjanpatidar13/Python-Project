# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:56:32 2019

@author: Administrator
"""

s=input("enter a string:")
dict={}
for i in s:
    dict[i]=dict.get(i,0)+1
print(dict)