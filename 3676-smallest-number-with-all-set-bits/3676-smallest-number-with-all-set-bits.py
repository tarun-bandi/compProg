class Solution:
    def smallestNumber(self, n: int) -> int:
        

        for i in range(1, 11):
            candidate = 2 ** i - 1 
            if candidate >= n:
                return candidate
        
        raise ValueError("Hell naw")