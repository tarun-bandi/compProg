class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        inDegree = defaultdict(int)

        meetings.sort(key = lambda x: x[2])
        has_secret = set()

        has_secret.add(0)
        has_secret.add(firstPerson)

        i = 0
        while i < len(meetings):
            x, y, t = meetings[i]
            curr_graph = defaultdict(list)
            while i < len(meetings) and t == meetings[i][2]:
                x, y, _ = meetings[i]
                curr_graph[x].append(y)
                curr_graph[y].append(x)
                i += 1
            queue = deque()
            for node in curr_graph:
                if node in has_secret:
                    queue.append(node)
            seen = set()
            while queue:
                node = queue.popleft()
                if node not in seen:
                    seen.add(node)
                    for neighbor in curr_graph[node]:
                        queue.append(neighbor)
                        has_secret.add(neighbor)


        return list(has_secret)