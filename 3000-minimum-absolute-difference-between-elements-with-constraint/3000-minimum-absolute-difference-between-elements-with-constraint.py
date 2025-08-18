from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        
        sorted_list = SortedList()
        answer = float("inf")

        for i in range(len(nums)):

            if i >= x:
                valid_candidate = i - x
                sorted_list.add(nums[valid_candidate])
            
            index = sorted_list.bisect_left(nums[i])

            if index < len(sorted_list):
                answer = min(answer, abs(sorted_list[index] - nums[i]))
            if index - 1 >= 0:
                answer = min(answer, abs(sorted_list[index - 1] - nums[i]))
        
        return answer