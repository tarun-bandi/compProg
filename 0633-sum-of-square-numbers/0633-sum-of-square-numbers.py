class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        i = 0
        while i**2 <= c:
            if (c - i**2)**0.5 == int((c - i**2)**0.5):
                return True
            i += 1
            
        
        return False
