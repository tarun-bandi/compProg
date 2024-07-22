class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(amount, coin):
            print(amount, coin)
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            elif coin == len(coins):
                return 0
            
            return dfs(amount - coins[coin], coin) + dfs(amount, coin + 1)
        return dfs(amount, 0)
