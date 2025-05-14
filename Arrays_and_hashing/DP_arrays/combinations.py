class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(n, k, idx, curr, res):
            if len(curr) == k:
                res.append(curr[:])
                return 
            if idx > n:
                return 
            # pick
            curr.append(idx)
            helper(n, k, idx+1, curr, res)
            curr.pop()

            #don't pick
            helper(n, k, idx+1, curr, res)
            
        helper(n, k, 1, [], res)
        return res 
