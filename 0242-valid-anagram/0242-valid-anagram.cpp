class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_counts;
        std::unordered_map<char, int> t_counts;

        for (char c : s){
            s_counts[c]++;
        }

        for (char c : t){
            t_counts[c]++;
        }

        for (const auto& key_value : s_counts){
            char key = key_value.first;
            if (s_counts[key] != t_counts[key]){
                return false;
            }
        }

        for (const auto& key_value : t_counts){
            char key = key_value.first;
            if (s_counts[key] != t_counts[key]){
                return false;
            }
        }

        return true;
    }
};