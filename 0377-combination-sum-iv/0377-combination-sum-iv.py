class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(curr_target: int) -> int:
            if curr_target == target:
                return 1
            if curr_target > target:
                return 0

            res = 0
            for n in nums:
                res += dp(curr_target + n)
            
            return res
        
        return dp(0)
