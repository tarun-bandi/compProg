class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        lo = 0
        hi = len(nums) - 1
        if len(nums) == 1:
            return 0

        def is_peak(index: int):
            if index == 0 and nums[0] > nums[1]:
                return True
            
            if index == len(nums) - 1 and nums[index] > nums[index - 1]:
                return True
            
            if nums[index] > nums[index - 1] and nums[index] > nums[index + 1]:
                return True
            
            return False
        
        while lo < hi:
            mid = (lo + hi) // 2
            if is_peak(mid):
                return mid
            
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo

        