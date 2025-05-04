from typing import List

"""
Recursive solution 
Time complexity : O(2^n)
Space complexity : O(n)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, idx, curr, res):
            if idx == len(nums):
                res.append(curr[:])
                return 
            #inc 
            curr.append(nums[idx])
            helper(nums, idx+1, curr, res)
            curr.pop()
            #exc 
            helper(nums, idx+1, curr, res)
        helper(nums, 0, [], res)
        return res 