# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:38:13 2019

@author: akash
"""
nums=[-1,0,1,2,-1,-4]
res = []
nums.sort()
hashes = set()
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    l, r = i + 1, len(nums) - 1
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < 0:
            l += 1
        elif s > 0:
            r -= 1
        else:
            a = [nums[i], nums[l], nums[r]]
            h = "".join(map(str, a))
            if h not in hashes:
                res.append(a)
                hashes.add(h)
                l += 1; r -= 1
print(res)