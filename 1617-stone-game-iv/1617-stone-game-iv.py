class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @cache
        def dp(i: int):
            if i == 0:
                return False
            square = 1
            possible = False
            while square ** 2 <= i:
                possible = possible or (not dp(i - square ** 2))
                square += 1

            return possible
        
        return dp(n) > 0
