class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        @cache
        def dp(x, y):
            if x >= len(grid) or y >= len(grid[0]):
                return float("inf")
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return grid[x][y]
            
            curr_path_size = float("inf")

            dirs = [(0, 1), (1, 0)]

            for dx, dy in dirs:
                curr_path_size = min(curr_path_size, dp(x + dx, y + dy))
            
            return curr_path_size + grid[x][y]
        
        return dp(0, 0)
