class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        next1 = 0
        next2 = 0
        for i in range(n - 1, -1, -1):
            curr = cost[i] + min(next1, next2)
            next2 = next1
            next1 = curr
        print(next1, next2)
        return min(next1, next2)  # dp[0], dp[1]