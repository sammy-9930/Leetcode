"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums

example: nums = [1,1,2]
o/p = 2 
nums = [1,2,_]
"""

def remove_duplicates(arr):
    j = 0 
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j += 1 
    return j 


arr = [1, 1, 2]
print(f"Count of unique elements: {remove_duplicates(arr)}")