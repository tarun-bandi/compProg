class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        order = []

        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = collections.deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        

        while queue:
            current_course = queue.popleft()
            order.append(current_course)
            for successor in graph[current_course]:
                indegree[successor] -= 1

                if indegree[successor] == 0:
                    queue.append(successor)        

        return order if len(order) == numCourses else []
        

        



