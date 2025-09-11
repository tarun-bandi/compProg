class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n: int = len(nums)
        LIS_ending_at = [0 for _ in range(len(nums))]
        LIS_ending_at[0] = 1

        for i in range(1, n):
            longest_subsequence_before = 0
            for candidate in range(0, i):
                if nums[candidate] < nums[i]:
                    longest_subsequence_before = max(longest_subsequence_before, LIS_ending_at[candidate])
            LIS_ending_at[i] = longest_subsequence_before + 1
        
        return max(LIS_ending_at)

        @cache
        def find_LIS_ending_at(index: int) -> int:
            if index >= len(nums):
                return 0

            longest_subsequence_before = 0
            for candidate in range(0, index):
                if nums[candidate] < nums[index]:
                    longest_subsequence_before = max(longest_subsequence_before, find_LIS_ending_at(candidate))

            return 1 + longest_subsequence_before

        longest_subseq = float("-inf")

        # Look through all endpoints
        for i in range(len(nums)):
            longest_subseq = max(longest_subseq, find_LIS_ending_at(i))

        return longest_subseq
