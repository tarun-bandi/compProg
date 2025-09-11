class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        paths_from_origin_to = [[1] * (n + 1) for _ in range(m + 1)]

        for i in range(2, m + 1):
            for j in range(2, n + 1):
                paths_from_origin_to[i][j] = paths_from_origin_to[i - 1][j] + paths_from_origin_to[i][j - 1]
        
        return paths_from_origin_to[m][n]
        @cache
        def find_path_from_origin_to(x: int, y: int) -> int:
            if x == 1 or y == 1: 
                return 1
            return find_path_from_origin_to(x - 1, y) + find_path_from_origin_to(x, y - 1)
        
        return find_path_from_origin_to(m, n)

