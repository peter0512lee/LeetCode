class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        q = deque((row, 0) for row in range(rows))
        dist = [[0] * cols for _ in range(rows)]
        directions = ((-1, 1), (0, 1), (1, 1))

        while q:
            i, j = q.popleft()
            for d in directions:
                new_row, new_col = i + d[0], j + d[1]

                if (
                    0 <= new_row < rows and
                    0 <= new_col < cols and
                    grid[i][j] < grid[new_row][new_col] and
                    dist[new_row][new_col] < dist[i][j] + 1
                ):
                    dist[new_row][new_col] = dist[i][j] + 1
                    ans = max(ans, dist[new_row][new_col])
                    q.append((new_row, new_col))

        return ans
