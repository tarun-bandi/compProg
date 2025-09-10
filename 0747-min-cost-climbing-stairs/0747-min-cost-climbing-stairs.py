class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        a, b = cost[0], cost[1]  # a = dp[i-2], b = dp[i-1]
        for i in range(2, n):
            a, b = b, cost[i] + min(a, b)
        return min(a, b)
