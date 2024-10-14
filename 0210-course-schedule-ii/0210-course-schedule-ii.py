class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        indegree = defaultdict(int)

        for second, first in prerequisites:
            graph[first].append(second)
            indegree[second] += 1
        
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        ordering = [0] * numCourses
        current_course = 0
        while queue:
            finished = queue.popleft()
            ordering[current_course] = finished
            for neighbor in graph[finished]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            current_course += 1
        
        return ordering if current_course == numCourses else []

