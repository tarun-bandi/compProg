class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        idx = 0 

        while idx < len(nums):
            current_value = nums[idx]
            if 0 < nums[idx] <= len(nums) and nums[idx] != nums[current_value - 1] :
                nums[idx], nums[current_value - 1] = nums[current_value - 1], current_value
            else:
                idx += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
                