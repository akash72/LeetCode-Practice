# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:11:09 2019

@author: akash
"""

x = [1,4,5,7,9,6,2]
target = 9
for i in x:
    if i < target:
        pair = int(target) - int(i)
        if pair in x:
            print ("the first number= %d the second number %d"%(i,pair))
            break