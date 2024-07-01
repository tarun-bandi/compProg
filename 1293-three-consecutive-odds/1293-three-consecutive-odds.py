class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cons = 0

        for c in arr:
            if c % 2 == 1:
                cons += 1
            else:
                cons = 0
            if cons == 3:
                return True
        return False
        