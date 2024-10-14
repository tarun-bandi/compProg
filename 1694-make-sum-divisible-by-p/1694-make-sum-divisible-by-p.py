class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        
        target = sum(nums) % p
        
        if target == 0: return 0

        mods = dict()
        mods[0] = -1
        n = len(nums)
        currSum = 0
        min_len = n

        for i in range(n):
            currSum = (currSum + nums[i]) % p
            needed = (currSum - target) % p
            if needed in mods:
                min_len = min(min_len, i - mods[needed])
            
            mods[currSum] = i
        
        return -1 if min_len == n else min_len


