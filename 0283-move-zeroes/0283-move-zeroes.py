class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur0 = i = 0

        while i < len(nums):
            if nums[cur0] != 0:
                cur0 += 1
                i += 1
            elif nums[i] != 0:
                nums[cur0], nums[i] = nums[i], nums[cur0]
                cur0 += 1
                i += 1
            elif nums[cur0] == 0:
                i += 1
        
        