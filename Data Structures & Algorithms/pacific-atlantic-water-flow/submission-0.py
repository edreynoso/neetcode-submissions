class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac = set()
        atl = set()

        def dfs(i, j, h, v ):

            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            if (i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0])
             or (i,j) in v or heights[i][j] < h):
                return

            v.add((i,j))

            dfs(i+1, j, heights[i][j], v)
            dfs(i-1, j, heights[i][j], v)
            dfs(i, j+1, heights[i][j], v)
            dfs(i, j-1, heights[i][j], v)
            

        for i in range(len(heights[0])):

            dfs(0,i, heights[0][i], pac)
            dfs(len(heights) -1, i, heights[len(heights) -1][i], atl)

        for i in range(len(heights)):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, len(heights[0]) -1, heights[i][len(heights[0])-1], atl)

        path = []

        for i in range(len(heights)):

            for j in range(len(heights[0])):

                if (i,j) in pac and (i,j) in atl:

                    path.append([i,j])
        
        return path