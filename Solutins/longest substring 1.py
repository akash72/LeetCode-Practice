# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:51:14 2019

@author: akash
"""
s="abcabcaa"
d={}
res=i=j=0
for m in s:
    if m in d:
        if i > d[m]:
            i=i 
        else:
            i=d[m]
    if res >=(j-i+1):
        res=res
    else:
        res=(j-i+1)
    d[m]=j+1
    j+=1
print(res)
   

            
   


