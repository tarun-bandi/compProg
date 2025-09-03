class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        # Count houses

        houses = [(x, y) for x in range(M) for y in range(N) if grid[x][y] == 1]

        houses_seen = [[0 for _ in range(N)] for _ in range(M)]
        distances = [[0 for _ in range(N)] for _ in range(M)]
        neighbors = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        def can_visit(x: int, y: int, house_number) -> bool:
            return 0 <= x < M and 0 <= y < N and houses_seen[x][y] == house_number - 1 and grid[x][y] == 0

        def bfs(x: int, y: int, house_number: int) -> None:
            # Make a queue
            to_visit = collections.deque()
            to_visit.append((x, y, 0))

            # While queue
            while to_visit:
                r, c, distance = to_visit.popleft()

                if houses_seen[r][c] == house_number:
                    continue
                houses_seen[r][c] += 1
                distances[r][c] += distance
                # find neighbors of elements

                for dx, dy in neighbors:
                    new_x, new_y = r + dx, c + dy
                    # if cell hasnt been visited & house is valid visit cell and add to q
                    if can_visit(new_x, new_y, house_number):
                        to_visit.append((new_x, new_y, distance + 1))

        # for each house, run BFS
        for i, (x, y) in enumerate(houses):
            bfs(x, y, i + 1)
        # check the grid, for each cell, see the distances
        min_dist = float("inf")

        for x in range(M):
            for y in range(N):
                if grid[x][y] == 0 and houses_seen[x][y] == len(houses):
                    min_dist = min(min_dist, distances[x][y])
        return min_dist if min_dist != float("inf") else -1
        # return if not seen.
