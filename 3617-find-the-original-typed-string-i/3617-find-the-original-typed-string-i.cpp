class Solution {
public:
    int possibleStringCount(string word) {
        char prev_char = word[0];
        int prev_index = 0;
        int totalPossibleStrings = 0;
        for (int i = 1; i < word.length(); i++){
            char cur_char = word[i];
            if (prev_char != cur_char){
                cout << "end of a run: " << prev_char << ". Run length: " << (i - prev_index) << std::endl;
                prev_char = cur_char;
                totalPossibleStrings += (i - prev_index - 1);

                prev_index = i;

            } 
        }
        cout << "end of a run: " << prev_char << ". Run length: " << (word.length() - prev_index) << std::endl;
        totalPossibleStrings += (word.length() - prev_index - 1);
        return totalPossibleStrings + 1;
    }
};