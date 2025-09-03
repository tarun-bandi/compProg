import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        lo = 0

        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        first = lo

        lo = 0

        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        last = hi

        if 0 <= first < len(nums) and first <= last and nums[first] == target:
            return [first, last]
        return [-1, -1]
