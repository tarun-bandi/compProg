class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        std::unordered_map<std::string, vector<std::string>> groups;
        
        for (std::string current_string : strs ){
            std::string key = current_string;
            std::sort(key.begin(), key.end());
            groups[key].push_back(current_string);
        }

        std::vector<std::vector<std::string>> result; 
        
        for (auto key_value : groups){
            result.push_back(key_value.second);
        }
        return result;
    }
};