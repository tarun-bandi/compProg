class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def count_ways(n: int):
            if n == 0:
                return 1
            if n == 1:
                return 1

            return count_ways(n - 1) + count_ways(n - 2)
        
        return count_ways(n)