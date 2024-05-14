class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[y][x] == 0:
                return 0
            
            # Temporarily set current cell to 0 to mark it as visited
            gold = grid[y][x]
            grid[y][x] = 0

            # Explore all possible directions
            res = gold + max(dfs(x - 1, y), dfs(x + 1, y),
                         dfs(x, y - 1), dfs(x, y + 1))
            # Restore the current cell
            grid[y][x] = gold

            return res

        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(j, i))

        return ans