# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:51:14 2019

@author: akash
"""
s="abcabcaa"
sub=s[0]
long=sub
length=1
for i in s[1:]:
    if ord(sub[-1])<=ord(i):
        sub+=i
        if(len(sub)>length):
            length=len(sub)
            long=sub
    else:
        sub=i
print(long)
   

            
   


