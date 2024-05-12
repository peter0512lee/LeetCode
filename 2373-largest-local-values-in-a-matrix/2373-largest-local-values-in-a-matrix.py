class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]

        for row in range(1, n - 1):
            for col in range(1, n - 1):
                res[row - 1][col - 1] = 0
                for s_row in range(row - 1, row + 2):
                    for s_col in range(col - 1, col + 2):
                        res[row - 1][col - 1] = max(res[row - 1][col - 1], grid[s_row][s_col])        
        return res