class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<int, int> count;
        for (char task : tasks) {
            count[task]++;
        }

        priority_queue<int> readyTasks;
        for (auto& pair : count) {
            if (pair.second > 0) {
                readyTasks.push(pair.second);
            }
        }

        int time = 0;
        queue<pair<int, int>> cooldown;
        while (!readyTasks.empty() || !cooldown.empty()) {
            time++;

            if (readyTasks.empty()) {
                time = cooldown.front().second;
            } else {
                int count = readyTasks.top() - 1;
                readyTasks.pop();
                if (count != 0) {
                    cooldown.push({count, time + n});
                }
            }

            if (!cooldown.empty() && cooldown.front().second == time) {
                readyTasks.push(cooldown.front().first);
                cooldown.pop();
            }
        }

        return time;
    }
};