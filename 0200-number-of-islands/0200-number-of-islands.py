class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        seen = set()


        def dfs(x, y):
            if (0 <= x < len(grid) and 0 <= y < len(grid[0]) 
                and grid[x][y] == "1" and (x, y) not in seen):
                seen.add((x, y))
                res = 1
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    res += dfs(x + dx, y + dy) 
                return res
            return 0
        
        cc = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if dfs(x, y) > 0:
                    cc += 1
        
        return cc
                