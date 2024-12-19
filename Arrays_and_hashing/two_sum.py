"""
Brute force 
Time complexity : O(n2)
Space complexity: O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
"""
Hash Map
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for ind, value in enumerate(nums):
            diff = target - value 
            if diff in seen:
                return [seen[diff], ind]
            seen[value] = ind
        return []

"""
use enumerate to keep track of index and value at the same time. 
""" 