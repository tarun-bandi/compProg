class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> freq;
        for (char c : tasks)
            freq[c]++;

        // max-heap based on remaining frequency
        priority_queue<int> pq;
        for (auto& it : freq)
            pq.push(it.second);

        int time = 0;
        while (!pq.empty()) {
            int cycle = n + 1;  
            vector<int> tmp;

            // Try to execute up to (n+1) tasks in one cycle
            while (cycle > 0 && !pq.empty()) {
                int cnt = pq.top(); pq.pop();
                if (--cnt > 0) tmp.push_back(cnt);
                time++;
                cycle--;
            }

            // Push remaining tasks back
            for (int cnt : tmp) pq.push(cnt);

            // If pq is not empty, we need to account for idle time
            if (!pq.empty()) time += cycle;
        }

        return time;
    }
};
