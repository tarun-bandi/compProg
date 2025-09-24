class Solution {

struct pair_hash {
    size_t operator()(const std::pair<int,int>& p) const {
        return std::hash<int>()(p.first) ^ (std::hash<int>()(p.second) << 1);
    }
};
public:

    bool is_valid_cell(int x, int y, vector<vector<char>>& grid){
        if (x >= grid.size() || x < 0) return false;
        if (y >= grid[0].size() || y < 0) return false;

        if (grid[x][y] == '0') return false;

        return true; 
    }
    void bfs(int x, int y, unordered_set<pair<int, int>, pair_hash>& seen, vector<vector<char>>& grid){
        queue<pair<int, int>> q;
        q.push({x, y});

        while (!q.empty()){
            pair<int, int> curr_cell = q.front();
            q.pop();
            int i = curr_cell.first;
            int j = curr_cell.second;
            if (seen.find(curr_cell) != seen.end()){
                continue;
            }
            seen.insert(curr_cell); 

            vector<pair<int, int>> neighbors = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

            for (int k = 0; k < 4; ++k){
                pair<int, int> neighbor = neighbors[k];
                int new_i = i + neighbor.first;
                int new_j = j + neighbor.second;
                if (is_valid_cell(new_i, new_j, grid)){
                    q.push({new_i, new_j});
                }
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        
        int m = grid.size();
        int n = grid[0].size();
        unordered_set<pair<int, int>, pair_hash> seen;
        int cell_ct = 0;
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if (grid[i][j] == '1' && seen.find({i, j}) == seen.end()){
                    cell_ct++;
                    bfs(i, j, seen, grid);
                }
            }
        }

        return cell_ct;


    }
};

// auto init=atexit([]{ofstream("display_runtime.txt")<<"0";});