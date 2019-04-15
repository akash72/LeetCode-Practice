# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:51:14 2019

@author: akash
"""
nums=[1,3,5,7]
nums2=[4,5,8,9]
b=324
l2=list(reversed(nums))
print(l2)
l2 = ''.join(map(str, l2))
l2=int(l2)
print(l2)
l3=list(reversed(nums2))
l3 = ''.join(map(str, l3))
l3=int(l3)
print(l3)
sum = 0 
sum = l2+l3
print(sum)
x=[int(d) for d in str(sum)]
x=list(reversed(x))
print(x)


