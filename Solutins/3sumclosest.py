# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:41:26 2019

@author: akash
"""

num=[-1, 2, 1, -4]
target=1
num.sort()
result = num[0] + num[1] + num[2]
for i in range(len(num) - 2):
    j, k = i+1, len(num) - 1
    while j < k:
        sum = num[i] + num[j] + num[k]
        if sum == target:
            print(sum)
                
        if abs(sum - target) < abs(result - target):
            result = sum
                
        if sum < target:
            j += 1
        elif sum > target:
            k -= 1
            
print (result)
     
     