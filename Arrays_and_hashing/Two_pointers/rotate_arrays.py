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
        res = [-1]*len(nums)
        for i in range(len(nums)):
            if (i + k) >= len(nums) - 1:
                pos = (i + k) % len(nums)
            else:
                pos = (i + k)
            res[pos] = nums[i]
        nums[:] = res 

"""
Optimized approach
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        # handles case where k > len(nums)
        k = k % len(nums)
        def helper(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l = l + 1 
                r = r - 1 
            return nums
        # Step 1: Reverse the entire array
        helper(0, len(nums)-1)
        # Step 2: Reverse first k elements
        helper(0, k - 1)
        # Step 3: Reverse the rest
        helper(k, len(nums)-1)

        
        
        