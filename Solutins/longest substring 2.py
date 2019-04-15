# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:51:14 2019

@author: akash
"""
s="abababas"
d={}
res=i=j=0
for m in s:
    if m in d:
        i= i if i>d[m] else d[m]
    res= res if res>=(j-i+1) else (j-i+1)
    d[m]=j+1
    j+=1
print(res)
   

            
   


