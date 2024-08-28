class Solution {
public:
    int ROWS, COLS;
    const int directions[5] = {0, 1, 0, -1, 0};

    bool dfs(int i, int j, int mark, vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        if (grid1[i][j] == 0) return false;

        grid2[i][j] = mark;

        bool is_sub_island = true;

        for (int d = 0; d < 4; d++) {
            int next_x = i + directions[d], next_y = j + directions[d + 1];

            if (next_x < 0 || next_x >= ROWS || next_y < 0 || next_y >= COLS || grid2[next_x][next_y] != 1)
                continue;

            if (grid1[next_x][next_y] != 1)
                is_sub_island = false;

            if (!dfs(next_x, next_y, mark, grid1, grid2))
                is_sub_island = false;
        }

        return is_sub_island;
    }

    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        ROWS = grid1.size();
        COLS = grid1[0].size();
        int islands = 0, mark = 2;

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid2[i][j] == 1) {
                    islands += dfs(i, j, mark++, grid1, grid2);
                }
            }
        }

        return islands;
    }
};