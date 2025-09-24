class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> temp_and_idx;
        vector<int> result_temperatures(temperatures.size());

        for (int i = 0; i < temperatures.size(); ++i){
            int todays_temp = temperatures[i];
            
            while (!temp_and_idx.empty() && temp_and_idx.top().first < todays_temp){
                int colder_index = temp_and_idx.top().second;
                result_temperatures[colder_index] = i - colder_index;
                temp_and_idx.pop();
            }
            temp_and_idx.push({todays_temp, i});
        }
        
        // while (!temp_and_idx.empty()){
        //     int index = temp_and_idx.pop().second;
        // }

        return result_temperatures;
    }
};