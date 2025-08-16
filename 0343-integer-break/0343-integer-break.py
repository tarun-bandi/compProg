class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def recursivelyBreakInteger(n: int) -> int:
            if n == 1:
                return 1
            if n < 2:
                return 0
            if n == 2:
                return 1
            
            current_product = 0
            for i in range(2, n):
                current_product = max(current_product, i * recursivelyBreakInteger(n - i), i * (n - i))

            return max(current_product, recursivelyBreakInteger(n - 1))
        
        return recursivelyBreakInteger(n)
