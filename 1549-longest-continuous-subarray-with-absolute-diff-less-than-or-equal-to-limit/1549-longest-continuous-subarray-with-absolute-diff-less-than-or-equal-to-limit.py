from sortedcontainers import SortedDict


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = SortedDict()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            window[nums[right]] = window.get(nums[right], 0) + 1

            while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    window.pop(nums[left])

                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length