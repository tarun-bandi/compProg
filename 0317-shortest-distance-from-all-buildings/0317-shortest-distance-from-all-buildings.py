class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        buildings = collections.deque()

        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    buildings.append((r, c))
        
        solution_grid = [[0 for _ in range(M)] for _ in range(N)]
        def bfs(r: int, c: int, num: int):
            queue = collections.deque()

            queue.append((r, c, 0))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while queue:
                row, col, distance = queue.popleft()

                for dx, dy in directions:
                    if 0 <= row + dx < N and 0 <= col + dy < M and grid[row + dx][col + dy] == -(num - 1):
                        solution_grid[row + dx][col + dy] += distance + 1
                        queue.append((row + dx, col + dy, distance + 1))
                        grid[row + dx][col + dy] = -num

        for i, (r, c) in enumerate(buildings):
            bfs(r, c, i + 1)

        ans = float("inf")

        for r in range(N):
            for c in range(M):
                if grid[r][c] == -len(buildings):
                    ans = min(ans, solution_grid[r][c])
        
        print(grid)
        print(solution_grid, ans)
        return ans if ans != float("inf") else -1
        

                