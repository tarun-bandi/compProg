class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def bfs(r : int, c : int): 
            queue = deque()

            def is_invalid(r : int, c : int) -> bool:
                return (r, c) in visited or r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0
                    

            queue.append((r, c))
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            area = 0
            while queue:
                (r, c) = queue.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                area += 1
                for dx, dy in dirs:
                    x, y = r + dx, c + dy
                    if not is_invalid(x, y):
                        queue.append((x, y))
            
            return area
        largest = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == 1:
                    largest = max(largest, bfs(r, c))
        
        return largest



                
            
            