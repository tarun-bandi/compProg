from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = deque()
        visited = set()

        ROWS, COLS = len(mat), len(mat[0])

        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
        
        def is_valid_cell(x: int, y: int) -> bool:
            if x < 0 or x >= ROWS:
                return False
            
            if y < 0 or y >= COLS:
                return False
            
            if (x, y) in visited:
                return False
            
            return True

        updated_matrix = copy.deepcopy(mat)
        
        while queue:



            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            nq = deque()
            for _ in range(len(queue)):
                x, y, distance_to_nearest_zero = queue.popleft()
                if (x, y) in visited:
                    continue
                updated_matrix[x][y] = distance_to_nearest_zero
                visited.add((x, y))
                for dx, dy in dirs:
                    if is_valid_cell(x + dx, y + dy):
                        
                        nq.append((x + dx, y + dy, distance_to_nearest_zero + 1))
            queue = nq
            
        return updated_matrix
            

