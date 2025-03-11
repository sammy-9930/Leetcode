from typing import List 

"""
Using stack
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop 

"""
Using in-built function 
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        return s.reverse()
    

"""
Using two pointers 
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s)-1 
        while l < r:
            s[l], s[r] = s[r], s[l]
        l, r = l+1, r-1 
        
