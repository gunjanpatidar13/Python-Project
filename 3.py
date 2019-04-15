# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:26:40 2019

@author: Administrator
"""

a,b,c=input("Enter three numbers:").split()
if(a>b and a>c):
    print(a,"is Greatest")
elif(b>c and b>a):
    print(b,"is Greatest")
else:
    print(c,"is Greatest")