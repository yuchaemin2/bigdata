#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:55:42 2025

@author: chaemin
1. 2개의 리스트를 읽어서 공통된 데이터가 있으면 True, 아니면 None을 반환하는 프로그램
을 작성하여라
"""


def common_data(list1, list2):
    n=0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if(list1[i] == list2[j]):
                n=n+1
            
    if(n>0):
        return True
   
        
    
    

print(common_data([1,2,3,4,5], [5,6,7,8,9])) # => True
print(common_data([1,2,3,4,5], [6,7,8,9]))   # => False

