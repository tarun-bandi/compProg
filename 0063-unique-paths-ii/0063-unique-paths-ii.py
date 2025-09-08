class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        @cache
        def dp(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                return 1 if obstacleGrid[i][j] != 1 else 0
            if i == m - 1:
                return dp(i, j + 1) if obstacleGrid[i][j + 1] != 1 else 0
            if j == n - 1:
                return dp(i + 1, j) if obstacleGrid[i + 1][j] != 1 else 0

            return (dp(i, j + 1) if obstacleGrid[i][j + 1] != 1 else 0) + (dp(i + 1, j) if obstacleGrid[i + 1][j] != 1 else 0)
        return dp(0, 0)
