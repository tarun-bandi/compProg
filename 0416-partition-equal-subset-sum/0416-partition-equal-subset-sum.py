class Solution:
    def canPartition(self, nums : List[int]) -> bool:
        target = sum(nums) // 2 
        if sum(nums) % 2 == 1:
            return False
        
        @cache
        def can_get(i: int, s: int):
            if s == target:
                return True
            if i == len(nums):
                return False
            
            return can_get(i + 1, s + nums[i]) or can_get(i + 1, s)
        print(target)
        return can_get(0, 0)