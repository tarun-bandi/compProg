class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = -1
        
        idx = 0

        while idx < len(nums):
            current_element = nums[idx]

            if current_element == -1:
                idx += 1
                continue
            if current_element != idx + 1 and nums[idx] != nums[current_element - 1]:
                nums[idx], nums[current_element - 1] = nums[current_element - 1], current_element
            else:
                idx += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
                