class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev = nums[0]
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] > prev:
                lo = mid + 1
            else:
                hi = mid
                prev = nums[mid]
        return prev

        