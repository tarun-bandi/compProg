from sortedcontainers import SortedDict
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        window = SortedDict()
        left = 0
        longest_window = 0
        for r in range(len(nums)):
            window[nums[r]] = window.get(nums[r], 0) + 1

            while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit:

                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            longest_window = max(longest_window, r - left + 1)
        return longest_window

