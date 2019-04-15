# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:30:35 2019

@author: akash
"""

a=[-1, 0, 1, 2, -1, -4]
target=0
a.sort()
b=len(a)
result=[]
for i in range(b-2):
    left_pointer=i+1
    right_pointer=b-1
    while(left_pointer<right_pointer):
        sum=a[i]+a[left_pointer]+a[right_pointer]
      
        if(sum<target):
            left_pointer+=1
        elif(sum>target):
            right_pointer-=1
        else:
            result.append([a[i],a[left_pointer],a[right_pointer]])
            left_pointer+=1
unique_lst = []
[unique_lst.append(sublst) for sublst in result if not unique_lst.count(sublst)]
print(unique_lst)
       

            
        
    
