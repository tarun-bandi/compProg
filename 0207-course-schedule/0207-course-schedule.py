class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for src, dst in prerequisites:
            graph[src].append(dst)
        
        def dfs(course, visited, path, graph):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            visited.add(course)
            for next_course in graph[course]:
                if not dfs(next_course, visited, path, graph):
                    return False
            path.remove(course)
            return True 
        def topological_sort(graph):
            visited, path = set(), set()
            for course in range(0, numCourses):
                if not dfs(course, visited, path, graph):
                    return False
            return True 
        
        
        return topological_sort(graph)
        