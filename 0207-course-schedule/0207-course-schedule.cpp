class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> graph;

        // Prereq is [(0, 1), (1, 2), ... , (3, 1)]
        unordered_set<int> indegree_zero;
        unordered_map<int, int> indegrees;

        for (int i = 0; i < numCourses; ++i)
            indegree_zero.insert(i);
        
        
        for (vector<int>& course_pair : prerequisites){
            int successor = course_pair[0];
            int prereq = course_pair[1];
            graph[prereq].push_back(successor);
            indegree_zero.erase(successor);
            indegrees[successor] += 1;
        }
        queue<int> ordering;
        for (auto& node : indegree_zero){
            ordering.push(node);
        }
        int nodes_seen = 0;
        while (!ordering.empty()){
            int curr_node = ordering.front();
            ordering.pop();
            nodes_seen++;

            for (int neighbor : graph[curr_node]){
                indegrees[neighbor]--;
                if (indegrees[neighbor] == 0){
                    ordering.push(neighbor);
                }
            }
        }
        return nodes_seen == numCourses;
    }
};