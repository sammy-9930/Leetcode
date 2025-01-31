from typing import List

"""
Brute force 
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans


"""
One pass solution
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        for i in range(n):
            ans[i] = ans[n+i] = nums[i]
        return ans