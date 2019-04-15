# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:51:14 2019

@author: akash
"""
l1=[1,2,]
l2=[3,4]
sum=0
l3=l1+l2
l3=sorted(l3)
print(l3)
z=len(l3)
mid=z/2
mid=int(mid)
if z%2==0:
    print(l3[mid])
    print(l3[mid-1])
    x=l3[mid]+l3[mid-1]
    y=x/2
    sum=y
else:
    sum=l3[mid]
print(sum)
    
   

            
   


