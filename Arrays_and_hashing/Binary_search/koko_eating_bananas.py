"""
Brute force
Time limit exceeded
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for i in range(1, max(piles)+1):
            hours = 0 
            for pile in piles:
                hours += pile // i 
                if pile % i != 0:
                    hours += 1 
            if hours <= h:
                return i


""" using binary search """
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            hours = 0 
            m = (l + r)//2
            for pile in piles:
                hours += pile // m 
                if pile % m != 0:
                    hours += 1 
            if hours <= h:
                r = m 
            else:
                l = m+1 
        return l