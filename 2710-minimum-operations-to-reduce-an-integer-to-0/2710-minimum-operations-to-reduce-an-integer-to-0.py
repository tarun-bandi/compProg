class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0
        while n > 0:
            if n & 1 == 0:
                n >>= 1
            elif n & 3 == 1:
                n -= 1
                operations += 1
            else:
                n += 1
                operations += 1
        return operations