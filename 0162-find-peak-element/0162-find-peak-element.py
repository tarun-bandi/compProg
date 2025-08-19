class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # We want to binary search bc of the log(n) time
        # We know we are a peak when we are bigger then the 2 elements next to us
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