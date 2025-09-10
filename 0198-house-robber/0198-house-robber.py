class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            take = nums[i] + dp[i + 2]
            dont_take = dp[i + 1]
            dp[i] = max(take, dont_take)
        
        return dp[0]
        
        @cache
        def dp(i: int):
            if i >= len(nums):
                return 0
            take = nums[i] + dp(i + 2)
            not_take = dp(i + 1)
            return max(take, not_take)
        
        return dp(0)