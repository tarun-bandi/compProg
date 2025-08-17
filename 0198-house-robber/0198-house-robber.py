class Solution:
    def rob(self, nums: List[int]) -> int:
        """ Use a recursive DP solution to attack problem """
        
        @cache
        def rob_from(index: int) -> int:
            """ Solves the subproblem of max money from [index, end] """

            if index >= len(nums):
                return 0
            
            rob = nums[index] + rob_from(index + 2)
            dont_rob = rob_from(index + 1)
            return max(rob, dont_rob)
        
        return rob_from(0)