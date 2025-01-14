"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
def single_number(nums):
    res = 0 
    for number in nums:
        # 2 same number XOR  gives us zero 
        res = res ^ number 
    return res 

nums = [4,1,2,1,2]
print(single_number(nums))
