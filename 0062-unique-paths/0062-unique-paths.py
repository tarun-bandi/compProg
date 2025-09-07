class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def find_path_from_origin_to(x: int, y: int) -> int:
            if x == 1 or y == 1: 
                return 1
            return find_path_from_origin_to(x - 1, y) + find_path_from_origin_to(x, y - 1)
        
        return find_path_from_origin_to(m, n)

