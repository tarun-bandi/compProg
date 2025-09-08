class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        @cache
        def dp(i: int, j: int):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return 0

            if i == len(grid) - 1:
                return grid[i][j + 1] + dp(i, j + 1)
            if j == len(grid[0]) - 1:
                return grid[i + 1][j] + dp(i + 1, j)

            return min(grid[i][j + 1] + dp(i, j + 1), grid[i + 1][j] + dp(i + 1, j))

        return dp(0, 0) + grid[0][0]


