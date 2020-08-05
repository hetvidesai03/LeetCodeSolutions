class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        max_row= [max(row) for row in grid]
        
        max_col= []
        
        for i in range(len(grid[0])):
            column= [grid[row][i] for row in range(len(grid))]
            max_col.append(max(column))
            
        total=0
        
        for i, row in enumerate(grid):
            for j, column in enumerate(row):
                total+=min(max_row[i], max_col[j]) - grid[i][j]
                
        return total