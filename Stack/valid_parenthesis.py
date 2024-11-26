"""
Brute force 
Time complexity: O(n2)
Space complexity: O(n)
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''


"""
Stack
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        s_map = {')' : '(', '}' : '{', ']' : '['}
        for char in s:
            if char in s_map:
                if stack and stack[-1] == s_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return stack == []

        