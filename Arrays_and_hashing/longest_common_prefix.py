from typing import List

"""
Time complexity: O(n∗m)
m - no of strings 
n - length of shortest word
Space complexity: O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(prefix)):
            for word in strs:
                if i == len(word) or prefix[i] != word[i]:
                    return prefix[:i]
        return prefix