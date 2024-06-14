class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()

        min_not_seen = 0
        steps = 0
        for c in nums:
            if c > min_not_seen:
                min_not_seen = c + 1
            else:
                steps += (min_not_seen - c)
                min_not_seen += 1
        return steps



        

        