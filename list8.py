# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:19:48 2019

@author: Administrator
"""
list1=input("enter elements of list1:").split()
list2=input("enter elements of list2:").split()
def fun(list1,list2):
    for i in list1:
        if i in list2:
            return(True)
print(fun(list1,list2))