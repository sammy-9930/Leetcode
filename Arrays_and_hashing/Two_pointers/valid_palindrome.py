"""
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        res = []
        for char in s:
            if (ord(char) >= ord('a') and ord(char) <= ord('z') or 
               ord(char) >= ord('0') and ord(char) <= ord('9')):
               res.append(char)
        return res == res[::-1]
"""slicing similar for string and list. """



"""

Why use lists for operations and not strings 
Avoid string concatenation in a loop (res += char) — Strings are immutable in Python, so each += creates a new string. 
This is inefficient in terms of time and memory. Use a list and ''.join() at the end.

Use Python’s built-in isalnum() method instead of manually checking ASCII ranges.

"""

"""
Approach 2: using 2 pointers 
do not create new list, check in place 
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlp(char):
            return (ord('a') <= ord(char) <= ord('z') or 
                    ord('0') <= ord(char) <= ord('9'))
        s = s.lower()
        l, r = 0, len(s) - 1 
        while l < r:
            while l < r and not isAlp(s[l]):
                l = l + 1 
            while l < r and not isAlp(s[r]):
                r = r - 1 
            if s[l] != s[r]:
                return False 
            l, r = l+1, r-1 
        return True 