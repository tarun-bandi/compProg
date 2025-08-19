class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = collections.deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        answer = []  
        while queue:
            curr_course = queue.popleft()
            answer.append(curr_course)

            for successor in graph[curr_course]:
                indegree[successor] -= 1
                if indegree[successor] == 0:
                    queue.append(successor)
        
        return answer if len(answer) == numCourses else []
        

