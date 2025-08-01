class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()

        for i, c in enumerate(nums):
            if c not in complements:
                complements[target - c] = i
            else:
                return (i, complements[c])


        