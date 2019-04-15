# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:12:37 2019

@author: Administrator
"""

list=input("enter elements of list:").split()
fl=[]
for i in list:
    if i not in fl:
        fl.append(i)
print("list=",fl)
