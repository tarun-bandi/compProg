class Solution {
private:
    int directions[4][2] = {{1, 0}, {-1, 0},
                                {0, 1}, {0, -1}};
    bool is_valid(vector<vector<char>>& grid, int x, int y){
        if (x < 0 || x >= grid.size()) return false;
        if (y < 0 || y >= grid[0].size()) return false;
        if (grid[x][y] == '0') return false;
        return true;
    }
    void bfs(vector<vector<char>>& grid, int x, int y){
        queue<pair<int, int>> q;
        q.push({x, y});
        while ( !q.empty() ){
            auto node = q.front();q.pop();
            int row = node.first, col = node.second;
            if (grid[row][col] == '0') continue;
            grid[row][col] = '0';
            for(int i = 0; i < 4; ++i){
                int new_row = directions[i][0] + row;
                int new_col = directions[i][1] + col;

                if (is_valid(grid, new_row, new_col)){
                    q.push({new_row, new_col});
                }
            }
        }

    }
public:
    int numIslands(vector<vector<char>>& grid) {
        
        int n = grid.size();
        int m = grid[0].size();
        int cells = 0;
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                if (grid[i][j] == '1'){
                    bfs(grid, i, j);
                    ++cells;
                }
            }
        }
        return cells;
        
    }
};