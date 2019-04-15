# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:51:14 2019

@author: akash
"""
nums=[1,3,5,7]
target=10
dic={}
for i in range(len(nums)):
    dic[nums[i]]=i
for i in range(len(nums)):
    diff=target-nums[i]
    if diff in dic:
        if i != dic[diff]:
          print(i,dic[diff])
            

