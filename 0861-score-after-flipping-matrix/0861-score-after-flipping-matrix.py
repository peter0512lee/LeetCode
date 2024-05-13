class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # replace the row which has first 0
        for r in range(row):
            if grid[r][0] == 0:
                for c in range(col):
                    grid[r][c] ^= 1

        # count the number of 0s in columns
        for c in range(col):
            cnt = sum(grid[r][c] for r in range(row))
            if cnt < row - cnt:
                for r in range(row):
                    grid[r][c] ^= 1

        # sum the binary numbers in each row
        return sum([int(''.join(map(str, row)), 2) for row in grid])