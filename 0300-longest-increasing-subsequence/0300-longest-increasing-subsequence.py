class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]

        dp[0] = 1

        for i in range(1, len(nums)):
            maxVal = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxVal = max(maxVal, dp[j])
            dp[i] = maxVal + 1
        return max(dp)
