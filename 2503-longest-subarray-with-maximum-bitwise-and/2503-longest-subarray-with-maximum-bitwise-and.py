class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = max(nums)
        longest = 0
        curr_streak = 0
        for c in nums:
            if c == max_value:
                curr_streak += 1
            else:
                longest = max(longest, curr_streak)
                curr_streak = 0
            
        return max(longest, curr_streak)


        