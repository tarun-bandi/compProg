class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();

        vector<int> dp(n, -1);

        function<int(int)> find_cost_from_stair = [&] (int i) -> int {
            if (i >= n) return 0;
            if (dp[i] != -1) return dp[i];
            
            dp[i] = cost[i] + min(find_cost_from_stair(i + 1), find_cost_from_stair(i + 2));
            return dp[i];
        };

        return min(find_cost_from_stair(0), find_cost_from_stair(1));


    }
};