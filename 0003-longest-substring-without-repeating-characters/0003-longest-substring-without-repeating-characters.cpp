class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> freq_counts;
        int l = 0;
        int max_len = 0;
        for (int r = 0; r < s.size(); ++r){
            freq_counts[s[r]] ++;
            while (freq_counts[s[r]] > 1){
                freq_counts[s[l]]--;
                l++;
            }
            max_len = max(max_len, r - l + 1);
        }
        return max_len;
    }
};