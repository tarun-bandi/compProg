class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        farthest_jump = 0

        for i, n in enumerate(nums):
            if i <= farthest_jump:
                farthest_jump = max(farthest_jump, i + n)
        
        return farthest_jump >= len(nums) - 1