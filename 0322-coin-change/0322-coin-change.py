class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        @cache
        def dp(i: int, amt: int) -> int:
            if amt == 0:
                return 0
            if i == len(coins):
                return float("inf")
            take = float("inf")
            if coins[i] <= amt:
                take = dp(i, amt - coins[i]) + 1
            dont_take = dp(i + 1, amt)
            return min(take, dont_take)
        
        return dp(0, amount) if dp(0, amount) != float("inf") else -1


