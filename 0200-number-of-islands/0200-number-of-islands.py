class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        island_count = 0
        visited = set()

        def bfs(row, col):

            queue = deque()

            queue.append((row, col))
            directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
            while queue:
                x, y = queue.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if (new_x, new_y) in visited:
                        continue
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == "1":
                        queue.append((new_x, new_y))
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                print(r, c)
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_count += 1
                    bfs(r, c)
        return island_count




        