class Solution:
    def minDifference(self, nums: List[int]) -> int:
        negNums = []
        nums = sorted(nums)

        right = len(nums) - 1

        if len(nums) <= 4:
            return 0
        print(nums)
        #diff combinations
        #move left by 3 right by 0, 2 1, 1 2, 3 0
        return min(nums[-4] - nums[0], nums[-3] - nums[1], nums[-2] - nums[2], nums[-1] - nums[3])

