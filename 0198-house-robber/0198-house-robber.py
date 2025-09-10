class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dp(i: int):
            if i >= len(nums):
                return 0
            take = nums[i] + dp(i + 2)
            not_take = dp(i + 1)
            return max(take, not_take)
        
        return dp(0)