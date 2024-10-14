class Solution:
    def myPow(self, x: float, n: int) -> float:
        def doPow(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            else:
                p = doPow(x, n // 2)
                res = p * p if n % 2 == 0 else p * p * x
                return res
        
        if n < 0:
            return 1/doPow(x, -n)
        else:
            return doPow(x, n)
        
