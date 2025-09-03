#include <cctype>
class Solution {

public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while (l < r){
            while (!isalnum(s[l]) && l < r)
                l++;
            while (!isalnum(s[r]) && r > l)
                r--;
            if (l > r)
                return false;
            if (tolower(s[l]) != tolower(s[r]))
                return false;
            l++;
            r--;
        }
        return true;
    }
};