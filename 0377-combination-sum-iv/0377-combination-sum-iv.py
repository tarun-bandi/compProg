class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def count_combos(combo_sum) -> int:
            if combo_sum > target:
                return 0
            elif combo_sum == target:
                return 1

            res = 0
            for i in range(len(nums)):
                res += count_combos(combo_sum + nums[i])
            
            return res

            
        return count_combos(0)
        