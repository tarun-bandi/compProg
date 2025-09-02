class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        std::unordered_map<int, int> complements;

        for (int i = 0; i < nums.size(); i++){
            int num = nums[i];

            if (complements.find(num) != complements.end()){
                return {i, complements[num]};
            }
            complements[target - num] = i;
        }
        return {-1, 1};

    }
};