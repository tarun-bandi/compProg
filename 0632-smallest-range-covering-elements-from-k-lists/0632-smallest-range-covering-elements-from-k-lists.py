class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        min_heap = []
        k = len(nums)
        
        left = float('inf')
        right = float('-inf')
        
        # initialize heap and boundaries
        for i in range(k):
            val = nums[i][0]
            heapq.heappush(min_heap, (val, 0, i))
            left = min(left, val)
            right = max(right, val)
        
        res = [left, right]
        
        while True:
            val, idx, list_num = heapq.heappop(min_heap)
            
            # update best range
            if right - val < res[1] - res[0] or (right - val == res[1] - res[0] and val < res[0]):
                res = [val, right]
            
            # move forward in the popped list
            if idx + 1 == len(nums[list_num]):
                break
            new_val = nums[list_num][idx + 1]
            heapq.heappush(min_heap, (new_val, idx + 1, list_num))
            right = max(right, new_val)
        
        return res