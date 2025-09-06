class Solution {
private:
    int directions[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    
    struct pair_hash {
        size_t operator()(const pair<int,int>& p) const noexcept {
            return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
        }
    };

    unordered_map<pair<int, int>, int, pair_hash> longest_path_cache;

    
    bool is_valid_move(int i, int j, vector<vector<int>>& matrix, int current_cell){
        if (i < 0 || i >= matrix.size()) return false;

        if (j < 0 || j >= matrix[0].size()) return false;

        if (matrix[i][j] <= current_cell) return false;

        return true;

    }

    int longest_path_from_cell(int i, int j, vector<vector<int>>& matrix){
        if (longest_path_cache.find({i, j}) != longest_path_cache.end()){
            return longest_path_cache[{i, j}];
        }

        int longest_path = 1;

        for (int dir = 0; dir < 4; ++dir){
            int new_row = i + directions[dir][0];
            int new_col = j + directions[dir][1];
            if (is_valid_move(new_row, new_col, matrix, matrix[i][j]))
                longest_path = max(longest_path, 1 + longest_path_from_cell(new_row, new_col, matrix));
        }
        longest_path_cache[{i, j}] = longest_path;
        return longest_path;

    }
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size(); 
        int path_len = 0;
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < m; ++j){
                path_len = max(path_len, longest_path_from_cell(i, j, matrix));
            }
        }

        return path_len;
    }
};