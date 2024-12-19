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