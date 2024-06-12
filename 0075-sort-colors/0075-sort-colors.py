class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct = Counter(nums)
        pt = 0
        for i in range(3):
            print(pt)
            for _ in range(ct[i]):
                nums[pt] = i
                pt += 1


    
        
