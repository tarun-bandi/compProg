class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        curr_sum = 0
        ct = 0
        for c in nums:
            prefix_sums[curr_sum] += 1
            curr_sum += c
            comp = curr_sum - k
            ct +=  prefix_sums[comp]
        return ct
            