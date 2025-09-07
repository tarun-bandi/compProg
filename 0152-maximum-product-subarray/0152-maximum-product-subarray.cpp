class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int cur_min = 1;
        int cur_max = 1;
        int ans = nums[0];

        for (auto n : nums){
            if ( n == 0){
                cur_min = 1;
                cur_max = 1;
            }
            int old_max = cur_max * n;
            cur_max = max({cur_min * n , cur_max * n, n});
            cur_min = min({old_max, cur_min * n, n});
            ans = max(ans, cur_max);
        }

        return ans;
    }
};