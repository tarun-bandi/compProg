class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #Binary search

        def findFirstInstance(target, nums):
            lo = 0
            hi = len(nums)

            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else: #equal falls into this case
                    hi = mid

            return lo #if there is an issue check here
        
        def findLastInstance(target, nums):
            lo = 0
            hi = len(nums)

            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else: #equal falls into this case
                    hi = mid

            return lo - 1 #if there is an issue check here
        
        first = findFirstInstance(target, nums)
        last = findLastInstance(target, nums)
        if 0 <= first < len(nums) and nums[first] == target and 0 <= last < len(nums) and nums[last] == target:
            return [first, last]
        return [-1, -1]


