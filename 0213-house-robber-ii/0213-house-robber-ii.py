class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def rob_from(i: int, robbed_first: bool) -> int:
            """ Solves problem for nums[i:] """
            if i >= len(nums):
                return 0
            
            # Make sure circular case is handled
            if i == len(nums) - 1 and robbed_first:
                return 0
            
            return max(nums[i] + rob_from(i + 2, robbed_first), rob_from(i + 1, robbed_first))
        
        return max(rob_from(2, True) + nums[0], rob_from(1, False))

