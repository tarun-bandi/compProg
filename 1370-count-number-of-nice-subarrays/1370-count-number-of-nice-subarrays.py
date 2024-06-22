class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_ct = 0
        subarrays = 0
        l = 0
        ct = 0
        numbers_before_odd_count = 0
        for r in range(len(nums)):
            odd_ct += nums[r] % 2 
            if odd_ct == k:
                numbers_before_odd_count = 0
            while odd_ct == k:
                odd_ct -= nums[l] % 2
                numbers_before_odd_count += 1
                l += 1
            subarrays += numbers_before_odd_count
        return subarrays
