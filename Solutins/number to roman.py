# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:32:45 2019

@author: akash
"""
s="(({{}}))"
o="[{("
c="]})"
d={"]":"[","}":"{",")":"("}
a=[]
for n in s:
    if n in o:
        a.append(n)
    elif n in c:
        if len(a)==0:
            print("False")
        if a[-1]==d[n]:
            a.pop()
        else:
            print("false")
if (len(a)==0):
    print("ture")