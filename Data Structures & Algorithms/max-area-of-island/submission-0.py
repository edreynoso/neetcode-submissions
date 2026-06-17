class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):

            max_row = len(grid)
            max_col = len(grid[0])

            if (i < 0 or i >= max_row or j < 0 or j >= max_col or grid[i][j] == 0):
                return 0
            
            grid[i][j] = 0

            return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j+1) + dfs(i , j-1)


        max_area = 0

        for i in range(len(grid)):
            
            area = 0
            for j in range(len(grid[i])):

                if (grid[i][j] == 1):
                    area = dfs(i,j)
                

                max_area = max(max_area, area)
        
        return max_area