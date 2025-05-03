from typing import List

"""
Recursive solution -> 0 to n 
Time complexity: O(2^n)
Space complexity: O(n)
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(cost, idx):
            if idx >= len(cost):
                return 0
            return cost[idx] + min(helper(cost, idx+1), helper(cost, idx+2))
        return min(helper(cost, 0), helper(cost, 1))
    
"""
Recursive solution -> n to 0
Time complexity: O(2^n)
Space complexity: O(n)
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(cost, idx):
            if idx < 0: 
                return 0 
            return cost[idx] + min(helper(cost, idx-1), helper(cost, idx-2))
        return min(helper(cost, len(cost)-1), helper(cost, len(cost)-2))
