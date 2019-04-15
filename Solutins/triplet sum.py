# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:23:28 2019

@author: akash
"""

a=[1,2,3,4,5,6,7,8]
target=11
b=len(a)
q=[]
r=[]
for i in  range(0, b):
    s = set()
    curr_sum = target - a[i]
   
    for j in range(i+1,b):
        if (curr_sum - a[j]) in s:
            
           
            r.append([a[i],a[j],curr_sum-a[j]])
   
            
            
        s.add(a[j])
      

      #print(s)

print(r)
     