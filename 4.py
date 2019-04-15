# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:31:50 2019

@author: Administrator
"""

year=input("Enter the year:")
year=int(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("Leap Year")
else:
    print("Not a Leap Year")
    