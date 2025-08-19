from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:

        sl = SortedList()
        smallest_difference = float("inf")
        for i in range(len(nums)):
            if i >= x:
                sl.add(nums[i - x])
            if sl:
                closest_idx = sl.bisect_left(nums[i])
                closest_element = 0
                if closest_idx < len(sl):
                    closest_element = sl[closest_idx]
                    smallest_difference = min(smallest_difference, abs(closest_element - nums[i]))
                    
                closest_element = sl[closest_idx - 1]
                smallest_difference = min(smallest_difference, abs(closest_element - nums[i]))

                

        return smallest_difference


                
        