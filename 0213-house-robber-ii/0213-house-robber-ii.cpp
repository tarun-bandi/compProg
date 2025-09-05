class Solution {
public:

    int helper(vector<int> nums){
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];

        vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = max(nums[1], nums[0]);

        for (int i = 2; i < nums.size(); ++i){
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
        }
        return dp.back();
    }
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];

        vector<int> dp(nums.size() - 1, -1);
        vector<int> first_missing(nums.begin() + 1, nums.end());
        vector<int> last_missing(nums.begin(), nums.end() - 1);

        return max(helper(first_missing), helper(last_missing));

    }
};