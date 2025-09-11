class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def max_profit_starting_from(day: int, owned: bool):
            if day >= len(prices):
                return 0

            if owned:
                sell = max_profit_starting_from(day + 2, False) + prices[day]
                keep = max_profit_starting_from(day + 1, True)
                return max(sell, keep)
            else:
                buy = max_profit_starting_from(day + 1, True) - prices[day]
                keep = max_profit_starting_from(day + 1, False)
                return max(buy, keep)
        
        return max_profit_starting_from(0, False)