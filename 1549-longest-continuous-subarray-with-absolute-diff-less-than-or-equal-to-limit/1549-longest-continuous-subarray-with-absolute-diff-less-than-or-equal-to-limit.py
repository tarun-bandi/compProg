class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        min_queue = collections.deque()
        max_queue = collections.deque()
        left = 0
        length_subarray = 0

        for r in range(len(nums)):
            
            # Decreasing
            while max_queue and max_queue[-1] < nums[r]:
                max_queue.pop()
            max_queue.append(nums[r])

            #Increasing
            while min_queue and min_queue[-1] > nums[r]:
                min_queue.pop()
            min_queue.append(nums[r])

            while max_queue[0] - min_queue[0] > limit:

                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1
            
            length_subarray = max(length_subarray, r - left + 1)
        return length_subarray
