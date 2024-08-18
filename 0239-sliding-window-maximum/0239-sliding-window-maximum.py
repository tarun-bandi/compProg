class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        
        max_sliding_window = []
        dq = deque()

        for r in range(len(nums)):
            while dq and dq[-1][1] < nums[r]:
                dq.pop()
            dq.append((r, nums[r]))
            if dq[0][0] <= r - k:
                dq.popleft()
            if r >= k - 1:
                max_sliding_window.append(dq[0][1])


        return max_sliding_window


