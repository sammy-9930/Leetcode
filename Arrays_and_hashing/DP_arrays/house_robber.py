from typing import List 

"""
Recursive solution - 0 to n 
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, idx):
            if idx >= len(nums):
                return 0 
            rob = nums[idx] + helper(nums, idx+2)
            dont_rob = helper(nums, idx+1)
            return max(rob, dont_rob)
        return helper(nums, 0)
    
"""
Recursive solution: n to 0
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, idx):
            if idx < 0:
                return 0 
            rob = nums[idx] + helper(nums, idx - 2)
            dont_rob = helper(nums, idx - 1)
            return max(rob, dont_rob)
        return helper(nums, len(nums)-1)