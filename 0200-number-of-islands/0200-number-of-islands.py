from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW_COUNT = len(grid)
        COLUMN_COUNT = len(grid[0])

        island_counter = 0 
        island_cells_visited = set()
        
        def find_all_connected_cells(r, c):
            """
            This uses BFS to find all connected cells, using the overall 
            shared set for visited
            """
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            queue = deque()
            queue.append((r, c))

            def cell_is_unexplored(row, col):
                if row < 0 or row >= ROW_COUNT:
                    return False
                
                if col < 0 or col >= COLUMN_COUNT:
                    return False
                
                if grid[row][col] != "1" or (row, col) in island_cells_visited:
                    return False
                
                return True
            

            while queue:
                row, col = queue.popleft()

                if (row, col) in island_cells_visited:
                    continue

                island_cells_visited.add((row, col))
                
                # Look in all four directions
                for dx, dy in dirs:
                    if cell_is_unexplored(row + dx, col + dy):
                        queue.append((row + dx, col + dy))

            return

        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT):
                if grid[r][c] == "1" and (r, c) not in island_cells_visited:
                        find_all_connected_cells(r, c)
                        island_counter += 1
        
        return island_counter