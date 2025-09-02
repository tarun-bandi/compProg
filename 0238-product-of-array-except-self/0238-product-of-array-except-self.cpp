class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix_sums(n); 
        int prefix_prod = 1;

        for (int i = 0; i < n; i++){
            prefix_sums[i] = prefix_prod;
            prefix_prod *= nums[i];
        }

        vector<int> suffix_sums(n + 1); 
        int suffix_prod = 1;

        for (int i = n - 1; i >= 0; --i){
            suffix_sums[i] = suffix_prod;
            suffix_prod *= nums[i];
        }

        // cout << prefix_sums;

        vector<int> result(n);

        for (int i = 0; i < n; i++){
            result[i] = prefix_sums[i] * suffix_sums[i];
    
        }
        return result;


    }
};