from typing import List 

"""
Time complexity: O(nlogn)
Space complexity: O(1) or O(n) depending on the sorting algorithm.
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat_count = 0
        people.sort()
        l, r = 0, len(people) - 1 
        while l <= r:
            remain = limit - people[r]
            r -= 1 
            boat_count += 1 
            if l <= r and people[l] <= remain:
                l += 1 
        return boat_count 
