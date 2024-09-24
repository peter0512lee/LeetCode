class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] == "0":
                return

            grid[row][col] = "0"
            
            dfs(grid, row + 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row - 1, col)
            dfs(grid, row, col - 1)

        rows, cols = len(grid), len(grid[0])
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    islands += 1

        return islands