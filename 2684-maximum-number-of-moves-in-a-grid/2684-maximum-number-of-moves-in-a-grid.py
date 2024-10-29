class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        """
        using BFS to explore all possible distance and update the max moves
        """

        # initialize
        n_rows, n_cols = len(grid), len(grid[0])
        q = deque((row, 0) for row in range(n_rows))
        distances = [[0] * n_cols for _ in range(n_rows)]
        directions = [(-1, 1), (0, 1), (1, 1)]
        max_moves = 0

        while q:
            cur_x, cur_y = q.popleft()
            for dx, dy in directions:
                nxt_x, nxt_y = cur_x + dx, cur_y + dy
                
                # check the condition
                if (
                    0 <= nxt_x < n_rows and
                    0 <= nxt_y < n_cols and
                    grid[nxt_x][nxt_y] > grid[cur_x][cur_y] and
                    distances[nxt_x][nxt_y] < distances[cur_x][cur_y] + 1
                ):
                    distances[nxt_x][nxt_y] = distances[cur_x][cur_y] + 1
                    max_moves = max(max_moves, distances[nxt_x][nxt_y])
                    q.append((nxt_x, nxt_y))

        return max_moves