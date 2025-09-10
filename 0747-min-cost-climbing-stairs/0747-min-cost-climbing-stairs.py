class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dp(i: int) -> int:
            if i >= len(cost):
                return 0
            
            return min(dp(i + 1), dp(i + 2)) + cost[i]
        
        return min(dp(0), dp(1))