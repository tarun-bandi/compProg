class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = [None for _ in range(len(cost))]
        cache[-1] = cost[-1]
        cache[-2] = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            cache[i] = min(cache[i + 1], cache[i + 2]) + cost[i]
        
        return min(cache[0], cache[1])

            

        @cache
        def dp(i: int) -> int:
            if i >= len(cost):
                return 0
            
            return min(dp(i + 1), dp(i + 2)) + cost[i]
        
        return min(dp(0), dp(1))