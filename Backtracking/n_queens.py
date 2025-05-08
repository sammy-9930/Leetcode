from typing import List 

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(row, col, board, n):
            # horizontal left 
            for c in range(col):
                if board[row][c] == 'Q':
                    return False 
            # diagonal - bottom left 
            r, c = row, col 
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False 
                r += 1 
                c -= 1 
            # diagonal - top left
            r, c = row, col 
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False 
                r -= 1 
                c -= 1  
            return True 
        def helper(col, board, res, n):
            if col == n:
                res.append([''.join(row) for row in board])
                return 
            for row in range(n):
                if is_valid(row, col, board, n):
                    board[row][col] = 'Q'
                    helper(col+1, board, res, n)
                    board[row][col] = '.' 
        
        res = []
        board = [['.']*n for _ in range(n)]
        helper(0, board, res, n)
        return res 