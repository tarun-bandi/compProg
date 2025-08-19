class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def solve(nums):
            @cache
            def rob_from(i: int) -> int:
                if i >= len(nums):
                    return 0
                
                return max(rob_from(i + 2) + nums[i], rob_from(i + 1))
            return rob_from(0)
        
        return max(solve(nums[1:]), solve(nums[:-1]))
        
        