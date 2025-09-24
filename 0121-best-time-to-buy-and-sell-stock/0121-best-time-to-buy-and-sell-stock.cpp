class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int global_max {0};
        int l = 0;
        for (int r = 0; r < prices.size(); r++){
            if (prices[r] < prices[l])
                l = r;
            global_max = max(global_max, prices[r] - prices[l]);
        }
        return global_max;
    }
};