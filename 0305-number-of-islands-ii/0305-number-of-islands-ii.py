class Solution:
    class UnionFind:
        def __init__(self, n: int):
            self.ranks = [1 for _ in range(n)]
            self.parents = [i for i in range(n)]
        
        def find(self, x: int):
            if self.parents[x] != x:
                self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

        def union(self, x: int, y: int):
            root_x = self.find(x)
            root_y = self.find(y)
            
            if root_x == root_y:
                return 0  # Already connected
            
            if self.ranks[root_x] < self.ranks[root_y]:
                self.parents[root_x] = root_y
                self.ranks[root_y] += self.ranks[root_x]
            else:
                self.parents[root_y] = root_x
                self.ranks[root_x] += self.ranks[root_y]
            
            return 1  # Successfully merged two components

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = self.UnionFind(m * n)
        land = set()  # Track which cells are land
        island_count = 0
        res = []
        
        for x, y in positions:
            cell = x * n + y  # x * n + y, not x * m + y
            
            if cell in land:  # Already added
                res.append(island_count)
                continue
            
            land.add(cell)
            island_count += 1  # Start with a new island
            
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            
            for nx, ny in neighbors:
                if 0 <= nx < m and 0 <= ny < n:
                    neighbor_coord = nx * n + ny
                    if neighbor_coord in land:  # Only union with existing land
                        if uf.union(cell, neighbor_coord) == 1:
                            island_count -= 1  # Merged two islands into one
            
            res.append(island_count)
        
        return res