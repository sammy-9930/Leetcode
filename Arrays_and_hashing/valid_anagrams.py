"""
Hashmap implementation
time complexity: O(n)
space complexity: O(n)
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        s_map = {}
        for char in s:
            s_map[char] = 1 + s_map.get(char, 0)
        for char in t:
            if char in s_map:
                s_map[char] -= 1
        for key, value in s_map.items():
            print(key, value)
            if value > 0:
                return False 
        return True 
    
"""
Sorting 
time complexity : O(nlogn+mlogm)
space complexity: O(1) or O(n+m) depending on the sorting algorithm.
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
