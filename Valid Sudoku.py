import numpy as np
class Solution:
    
    def isValidNine(self, arr):
        arr = [ number for number in arr if number != '.']
        return len(arr) == len(set(arr))
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        board= np.array(board)
        
        for i in range(len(board)):
            row = board[i]
            column = board[:,i]
            if not self.isValidNine(row) or not self.isValidNine(column):
                return False

        for i in range(3):
            for j in range(3):
                box = board[i*3:(i+1)*3,j*3:(j+1)*3].flatten()
                if not self.isValidNine(box):
                    return False
        return True
