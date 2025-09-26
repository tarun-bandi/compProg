class Solution {
public:
    vector<vector<int>> dp;
    bool isMatch(string s, string p) {
        dp.assign(s.size() + 1, vector<int>(p.size() + 1, -1));
        return find_match_from(0, 0, s, p);
    }

    bool find_match_from(int i, int j, string& s, string& p){
        if (i >= s.size() && j >= p.size()) return true;
        if (j >= p.size()) return false;
        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        bool first_match = i < s.size() && (p[j] == '.' || s[i] == p[j]);

        if (j < p.size() - 1 && p[j + 1] == '*') {
            bool take = first_match && find_match_from(i + 1, j, s, p);
            bool dont_take = find_match_from(i, j + 2, s, p);
            dp[i][j] = take || dont_take;
            return take || dont_take;
        }
        dp[i][j] = first_match && find_match_from(i + 1, j + 1, s, p);
        return dp[i][j];
    }
};