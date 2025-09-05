class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        int n = nums.size();
        function<int(int)> find_house_robbed = [&] (int i) -> int {
            if (i >= n) return 0;
            if (dp[i] != -1) return dp[i];

            dp[i] = max(find_house_robbed(i + 1), nums[i] + find_house_robbed(i + 2));
            return dp[i];
        };

        return find_house_robbed(0);
    }
};