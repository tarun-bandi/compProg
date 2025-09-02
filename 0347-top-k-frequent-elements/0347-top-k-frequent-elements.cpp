class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();

        vector<vector<int>> buckets(n + 1);

        unordered_map<int, int> counts;

        for (auto num : nums){
            counts[num]++;
        }

        for (auto key_value : counts){
            int number = key_value.first;
            int count = key_value.second;
            buckets[count].push_back(number);
        }

        std::reverse(buckets.begin(), buckets.end());

        vector<int> result; 
        int i = 0;
        while (result.size() < k) {
            vector<int> current_bucket = buckets[i];
            result.insert(result.end(), current_bucket.begin(), current_bucket.end());
            i++;
        }

        return result;
        
        
    }
};