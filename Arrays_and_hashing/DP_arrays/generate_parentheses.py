class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(n, no_o, no_c, curr, res):
            if no_o == n and no_c == n:
                res.append(curr)
                return 
            # pick open 
            if no_o < n:
                helper(n, no_o+1, no_c, curr + '(', res)
            # pick close 
            if no_o > no_c:
                helper(n, no_o, no_c+1, curr + ')', res)
            
            
        helper(n, 0, 0, "", res)
        return res 