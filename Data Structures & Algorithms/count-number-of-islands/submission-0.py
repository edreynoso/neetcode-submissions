class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            row_max = len(grid)
            col_max = len(grid[0])

            if i < 0 or i >= row_max or j < 0 or j >= col_max or grid[i][j] == "0":
                return 0

            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

            return 1
            

        count = 0;
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    if dfs(i,j) > 0:
                        count +=1
        
        return count