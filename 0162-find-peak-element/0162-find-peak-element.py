class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            
            if mid != len(nums) - 1 and nums[mid] <= nums[mid + 1]:
                lo = mid + 1
            elif mid != 0 and nums[mid] <= nums[mid - 1]:
                hi = mid - 1
            else:
                return mid
        return -1