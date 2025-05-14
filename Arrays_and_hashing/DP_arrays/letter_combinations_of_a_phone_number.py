from typing import List 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi', 
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def helper(digits, idx, curr, res):
            if idx >= len(digits):
                res.append(''.join(curr))
                return
            for char in digit_map[digits[idx]]:
                curr.append(char)
                helper(digits, idx+1, curr, res)
                curr.pop()

        helper(digits, 0, [], res)
        return res 