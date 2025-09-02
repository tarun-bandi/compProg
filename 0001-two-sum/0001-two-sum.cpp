class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        std::unordered_map<int, int> complements;

        for (int i = 0; i < nums.size(); i++){
            int num = nums[i];
            auto complement_index = complements.find(num);
            if (complement_index != complements.end()){
                return {i, complement_index->second};
            }
            complements[target - num] = i;
        }
        
        auto dummy = {-1, 1};
        return dummy;

    }
};