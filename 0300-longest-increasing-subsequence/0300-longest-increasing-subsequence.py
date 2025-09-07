class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Subsequences = 2^n 
        # Greedy or Dynamic Programming approach

        # Subproblems: Subsequence ending at index i 

        @cache
        def find_LIS_ending_at(index: int) -> int:
            if index >= len(nums):
                return 0

            longest_subsequence_before = 0
            for candidate in range(0, index):
                if nums[candidate] < nums[index]:
                    longest_subsequence_before = max(longest_subsequence_before, find_LIS_ending_at(candidate))

            print(f"for {index}, longest_subseq_before is {longest_subsequence_before}")
            return 1 + longest_subsequence_before

        longest_subseq = float("-inf")

        # Look through all endpoints
        for i in range(len(nums)):
            longest_subseq = max(longest_subseq, find_LIS_ending_at(i))

        return longest_subseq
