# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:37:07 2019

@author: akash
"""

s="iamahappyperson"
numRows=3
l=len(s)
if numRows == 1:
    print(s)
solution = []
for i in range(0, numRows):
    count = i
    step1 = 2*(numRows-1-i)
    step2 = 2*i
    while count < len(s):
        solution.append(s[count])
        if step1 > 0 and step2 > 0 and count+step1<len(s):
            count += step1
            solution.append(s[count])
            count += step2
        else:
            count +=(step1+step2)
print( "".join(solution))