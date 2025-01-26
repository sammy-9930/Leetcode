from typing import List 

"""
Using extra space 
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*len(nums)
        for i in range(len(nums)):
            pos = i+k
            res[pos % len(nums)] = nums[i]
        nums[:] = res