"""
Time complexity: O(2^n)
Space complexity: O(n)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(text1, text2, idx1, idx2):
            # base 
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0 
            # if char are same - include the char in ans 
            if text1[idx1] == text2[idx2]: 
                return 1 + helper(text1, text2, idx1+1, idx2+1)
            # if not same 
            return max(helper(text1, text2, idx1+1, idx2), helper(text1, text2, idx1, idx2+1))
        return helper(text1, text2, 0, 0)