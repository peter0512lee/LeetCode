class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # initialize the m * n grid to track the ans
        grid = [[0] * n for _ in range(m)]

        # mark the guards and walls
        for r, c in guards:
            grid[r][c] = 2
        for r, c in walls:
            grid[r][c] = 3

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # calculate the not guarded 
        for r, c in guards:
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and grid[nr][nc] != 3:
                    grid[nr][nc] = 1
                    nr += dr
                    nc += dc

        return sum(c == 0 for r in grid for c in r)
