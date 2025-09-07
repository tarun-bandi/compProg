class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(i, sums):
            if i == len(nums):
                return 1 if sums == target else 0
            
            return dp(i + 1, sums - nums[i]) + dp(i + 1, sums + nums[i])
        
        return dp(0, 0)