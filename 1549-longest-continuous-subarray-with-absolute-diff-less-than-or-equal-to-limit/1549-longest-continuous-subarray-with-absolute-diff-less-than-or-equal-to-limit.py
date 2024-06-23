class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_heap = []
        max_heap = []

        l = 0
        max_len = 0
        for r in range(len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            heapq.heappush(min_heap, (nums[r], r))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                l = min(max_heap[0][1], min_heap[0][1]) + 1

                while max_heap[0][1] < l:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < l:
                    heapq.heappop(min_heap)
                
            max_len = max(max_len, r - l + 1)
        return max_len 

        