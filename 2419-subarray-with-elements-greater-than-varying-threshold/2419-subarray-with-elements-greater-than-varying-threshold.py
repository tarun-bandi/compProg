class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        
        stack = []

        left = [-1] * len(nums)
        right = [len(nums)] * len(nums)

        for i in range(len(nums)):
            n = nums[i]

            while stack and n <= stack[-1][0]:
                stack.pop()
            
            if stack:
                left[i] = stack[-1][1]
            stack.append((n, i))

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            while stack and n <= stack[-1][0]:
                stack.pop()
            if stack:
                right[i] = stack[-1][1]
            stack.append((n, i))

        for i in range(len(nums)):
            k = right[i] - left[i] - 1
            if k == 0:
                continue
            if nums[i] > threshold/k:
                return k
        
        return -1


