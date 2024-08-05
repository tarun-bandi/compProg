class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i : int, bought : int):
            if i >= len(prices):
                return 0
            if bought != -1:
                return max(dfs(i + 2, -1) + prices[i] - bought, dfs(i + 1, bought))
            else:
                return max(dfs(i + 1, prices[i]), dfs(i + 1, -1))
        
        return max(dfs(0, -1), 0)
