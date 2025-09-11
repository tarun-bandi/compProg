class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf")] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 0

        for i in range(len(coins) -1, -1, -1):
            for amt in range(1, amount + 1):
                take = float('inf')
                if coins[i] <= amt:
                    take = dp[i][amt - coins[i]] + 1
                dont_take = dp[i + 1][amt]
                dp[i][amt] = min(take, dont_take)
        
        return dp[0][amount] if dp[0][amount] != float('inf') else -1

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