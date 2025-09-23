class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // Count frequency of each task
        unordered_map<char, int> taskCounts;
        for (char task : tasks) {
            taskCounts[task]++;
        }
        
        // Find the maximum frequency
        int maxFreq = 0;
        for (auto& pair : taskCounts) {
            maxFreq = max(maxFreq, pair.second);
        }
        
        // Count how many tasks have the maximum frequency
        int maxFreqCount = 0;
        for (auto& pair : taskCounts) {
            if (pair.second == maxFreq) {
                maxFreqCount++;
            }
        }
        
        // Calculate minimum intervals needed
        // Framework: (maxFreq - 1) complete cycles, each needs (n + 1) slots
        // Plus final execution of all max frequency tasks
        int frameworkTime = (maxFreq - 1) * (n + 1) + maxFreqCount;
        
        // Result is at least the total number of tasks
        return max((int)tasks.size(), frameworkTime);
    }
};