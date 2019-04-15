# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:58:40 2019

@author: Administrator
"""

s=input("Enter words:").split()

for i in s:
    if(len(i)>1 and i[0]==i[-1]):
        count=count+1
print("count=:",count)