class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        @cache
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0

            max_amt = 0
            for k in range(i, j + 1):
                curr_amt = nums[i - 1] * nums[k] * nums[j + 1]
                curr_amt += dp(i, k - 1) + dp(k + 1, j)
                max_amt = max(max_amt, curr_amt)

            return max_amt

        return dp(1, n)