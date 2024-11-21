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
    
"""
Hashtable implementation 
time complexity: O(n+m)
space complexity: O(1)
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
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t

"""
Hashtable optimum 
time complexity: O(n+m) n,m are length of string s and t
space complexity: O(1) atmost 26 different characters 
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
        count = [0] * 26 
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 
            count[ord(t[i]) - ord('a')] -= 1 
        for value in count:
            if value > 0:
                return False 
        return True 
        
        