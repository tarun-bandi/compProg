class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maximum_profit = 0
        current_low = float(inf)
        for i in range(len(prices)):
            if prices[i] < current_low:
                current_low = prices[i]
            
            maximum_profit = max(maximum_profit, prices[i] - current_low)
        
        return maximum_profit
