class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        result = 0
        run_length = 0

        for i, c in enumerate(nums):
            if c == 0:
                run_length += 1
            else:
                print(i, run_length)
                result += ((run_length) * (run_length + 1)) /2
                run_length = 0
        result += ((run_length) * (run_length + 1)) /2

        return int(result)

