class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 2; ++i){
            if (nums[i] > 0){
                return result;
            }

            if (i != 0 && nums[i] == nums[i - 1]) continue;

            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r){
                if (l != i + 1 && nums[l] == nums[l - 1]) {
                    l++;
                    continue;
                }
                if (r != nums.size() - 1 && nums[r] == nums[r + 1]) {
                    r--;
                    continue;
                }
                if (nums[l] + nums[r] == -nums[i]){
                    result.push_back({nums[i], nums[l], nums[r]});
                    r--;
                    l++;
                } else if (nums[l] + nums[r] > -nums[i]) r--;
                else l++;
            }

        }

        return result;
    }
};