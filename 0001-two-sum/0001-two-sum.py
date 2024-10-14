class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        complement = dict()

        for i, c in enumerate(nums):
            if c in complement:
                return [complement[c], i]
            complement[target - c] = i
        
        return [-1, -1]
