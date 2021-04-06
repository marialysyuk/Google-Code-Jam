#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

def reversort(arr):
    maximum = len(arr)
    search = 1 
    count = 0 
    curr_i = 0
    while curr_i < len(arr)-1:
        for i in range(len(arr)):
            if arr[i] == search:
                count += i-curr_i+1
                arr[curr_i:i+1] = reversed(arr[curr_i:i+1])
                break
        curr_i += 1
        search += 1
    return count
    
nums = sys.stdin.readlines()

content = [[int(num) for num in line.split()] for line in nums]
content = content[1:]

cases = 0
i = 0 
while i < len(content):
    cases += 1
    arr = content[i+1]
    print("Case #"+str(cases)+": "+str(reversort(arr)))
    i += 2

