class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        minimum_elements = []
        left = float("inf")
        right = float("-inf")

        for i, num in enumerate(nums):
            element = num[0]
            heapq.heappush(minimum_elements, (element, i, 0)) # insert element, list_num, position in list
            left = min(left, element)
            right = max(right, element)

        res = [left, right]
        while True:
            _, list_num, pos = heapq.heappop(minimum_elements)
            if pos + 1 == len(nums[list_num]):
                return res
            
            pos += 1
            new_element = nums[list_num][pos]
            right = max(right, new_element)
            heapq.heappush(minimum_elements, (new_element, list_num, pos))
            left = minimum_elements[0][0]
            if right - left < res[1] - res[0]:
                res = [left, right]
        
        return -1


            
