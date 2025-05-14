from typing import List 

"""
Recursion 
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, idx, limit):
            if idx > limit:
                return 0 
            # inc cur pos 
            rob = nums[idx] + helper(nums, idx + 2, limit)
            # exc cur pos 
            dont_rob = helper(nums, idx + 1, limit)
            return max(rob, dont_rob)

        # 0 to n-1
        case_1 = helper(nums, 0, len(nums)-2)
        # 1 to n  
        case_2 = helper(nums, 1, len(nums)-1)
        return max(case_1, case_2)       