class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        left, right = float("inf"), float("-inf")
        pq = []

        for idx, sortedlist in enumerate(nums):
            first_element = sortedlist[0]

            heapq.heappush(pq, (first_element, idx, 0))

            left = min(left, first_element)
            right = max(right, first_element)
        
        result = [left, right]
        
        while True:
            _, list_number, pos = heapq.heappop(pq)

            pos += 1
            if pos >= len(nums[list_number]):
                return result

            next_element = nums[list_number][pos]

            heapq.heappush(pq, (next_element, list_number, pos))
            min_element = pq[0][0]
            left = min_element
            right = max(right, next_element)
        
            if right - left < result[1] - result[0]:
                result = [left, right]
        
        return -1




