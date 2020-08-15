class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def clearIsland(grid, i, j):
            if(grid[i][j]=="1"):
                grid[i][j] = "0"
                if(i>=1):
                    clearIsland(grid, i-1, j)
                if(j>=1):
                    clearIsland(grid, i, j-1)
                if(i<len(grid)-1):
                    clearIsland(grid, i+1, j)
                if(j<len(grid[i])-1):
                    clearIsland(grid, i, j+1)
        noOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]=="1"):
                    noOfIslands += 1
                    clearIsland(grid, i, j)
        return noOfIslands