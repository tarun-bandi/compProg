class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        oneCt, zeroCt = 0, 0

        maxCt = 0

        l = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroCt += 1
            else:
                oneCt += 1
            while zeroCt > k:
                if nums[l] == 0:
                    zeroCt -= 1
                else:
                    oneCt -= 1
                l += 1
            maxCt = max(maxCt, r - l + 1)
        
        return maxCt
                
