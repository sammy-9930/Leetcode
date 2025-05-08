class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, board, digit):
            #row
            for i in range(9):
                if board[row][i] == digit:
                    return False  
            #column 
                if board[i][col] == digit:
                    return False 
            #box 
                if(board[3*(row//3) + (i//3)][3*(col//3) + (i%3)] == digit):
                    return False
            return True 

        def helper():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for digit in '123456789':
                            if is_valid(row, col, board, digit):
                                board[row][col] = digit 
                                if helper():
                                    return True 
                                board[row][col] = '.' 
                        # return false because a previous placement caused this cell to become invalid
                        return False
            return True 

        helper()

            