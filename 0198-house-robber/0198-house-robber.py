class Solution:
    def rob(self, nums: List[int]) -> int:
        """ Use a recursive DP solution to attack problem """
        
        @cache
        def max_money_robbed_starting_from_house(index: int) -> int:
            """ Solves the subproblem of max money from [index, end] """

            if index >= len(nums):
                return 0
            
            rob_this_house = nums[index] + max_money_robbed_starting_from_house(index + 2)
            dont_rob_this_house = max_money_robbed_starting_from_house(index + 1)

            return max(rob_this_house, dont_rob_this_house)
        
        return max_money_robbed_starting_from_house(0)