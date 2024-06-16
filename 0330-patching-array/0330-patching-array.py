class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing = 0
        patches = 0

        for c in nums:
            while n > missing and c > missing + 1:
                missing += missing + 1
                patches += 1
            missing += c
        
        while n > missing:
            missing += missing + 1
            patches += 1
        return patches


        