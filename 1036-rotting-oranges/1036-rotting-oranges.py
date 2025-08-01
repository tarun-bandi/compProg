class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = collections.deque()
        orange_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    orange_count += 1
        if orange_count == 0:
            return 0
        minutes = 0
        #BFS
        while queue:
            minutes += 1
            # inner loop to empty queue
            new_rotten_oranges = deque()
            neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for (r, c) in queue:
                for dx, dy in neighbors:
                    x = r + dx 
                    y = c + dy
                    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
                        continue
                    new_rotten_oranges.append((x, y))
                    grid[x][y] = 2
                    orange_count -= 1
            
            if orange_count == 0:
                return minutes
            queue = new_rotten_oranges
        return -1
            
            
                
