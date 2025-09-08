class Solution:
    def integerBreak(self, n: int) -> int:

        def find_largest_product(N: int):
            if N <= 3:
                return N
            largest_prod = 0
            for i in range(2, N):
                largest_prod = max(largest_prod, find_largest_product(N - i) * i)
            return largest_prod

        if n <= 3:
            return n - 1
        return find_largest_product(n)
