class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0 for _ in range(n + 2)]
        dp_i2 = 0
        dp_i1 = 0

        for i in range(n - 1, -1, -1):
            take = nums[i] + dp_i2
            dont_take = dp_i1

            dp_i2 = dp_i1
            dp_i1 = max(take, dont_take)
        
        return dp_i1
        
        @cache
        def dp(i: int):
            if i >= len(nums):
                return 0
            take = nums[i] + dp(i + 2)
            not_take = dp(i + 1)
            return max(take, not_take)
        
        return dp(0)