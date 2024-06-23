class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #find the pivot

        lo = 0 
        hi = len(nums)
        curr_min = nums[0]
        min_idx = 0

        while lo < hi:
            mid = (lo + hi)//2

            if nums[mid] > curr_min:
                lo = mid + 1
            else:
                hi = mid
                curr_min = nums[mid]
                min_idx = mid

        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi)//2
            shifted = (mid + min_idx) % len(nums)
            if nums[shifted] == target:
                return shifted
            elif nums[shifted] > target:
                hi = mid
            else:
                lo = mid + 1
        return -1