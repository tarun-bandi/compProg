class Solution:
    def numSquares(self, n: int) -> int:
        
        squares = []

        i = 1

        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1

        @cache
        def dp(curr_sum: int):
            if curr_sum > n:
                return float("inf")
            if curr_sum == n:
                return 0

            total = float('inf')
            for square in squares:
                total = min(dp(curr_sum + square) + 1, total)
            return total

        return dp(0)