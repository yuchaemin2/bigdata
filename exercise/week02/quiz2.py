#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:06:16 2025

@author: chaemin
2. 문자열을 읽어서 리스트에 원소들이 있으면 True, 아니면 False를 반환하는 프로그램을
작성하여라
"""

def test(list,str):
    for i in range(len(list)):
        val = str.find(list[i])
        if(val!=-1):
            return True
        else:
            return False
   
    
"""   
def test(list,str):
    result=False
    str2 = str.split()
    for x in list:
        if x in str2:
            result=True
    return result
"""

str1 = "https://www.w3resource.com/python-exercises/list/"
lst = ['.com', '.edu', '.tv']
print(test(lst,str1))
str1 = "https://www.w3resource.net"
lst = ['.com', '.edu', '.tv']
print(test(lst,str1))