class Solution {
public:
    bool isMatch(string s, string p) {
        
   std::function<bool(int, int)> find_matches = [&](int i, int j) -> bool {
        if (j >= p.size()) return i >= s.size();
        
        bool first_match = (i < s.size()) && 
                          (p[j] == s[i] || p[j] == '.');
        
        if (j < p.size() - 1 && p[j + 1] == '*') {
            return find_matches(i, j + 2) || 
                   (first_match && find_matches(i + 1, j));
        } else {
            return first_match && find_matches(i + 1, j + 1);
        }
    };

    return find_matches(0, 0);


    }
};