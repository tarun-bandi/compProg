class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        visited = set()

        queue = collections.deque()

        queue.append((0, 0, k, 0))

        def is_valid(x, y, obs)-> Tuple[bool, int]:
            if x < 0 or x >= len(grid):
                return False, 0
            if y < 0 or y >= len(grid[0]):
                return False, 0
            if grid[x][y] == 0:
                return True, 0
            else:
                return obs > 0, 1
        while queue:
            x, y, obstacles, s = queue.popleft()
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return s
            if (x, y, obstacles) in visited:
                continue
            visited.add((x, y, obstacles))

            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for dx, dy in dirs:
                can_do, clear = is_valid(x + dx, y + dy, obstacles)
                if can_do:
                    queue.append((x + dx, y + dy, obstacles - clear, s + 1))
        
        return -1


