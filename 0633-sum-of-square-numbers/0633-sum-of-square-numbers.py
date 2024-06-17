class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqr_set = set()
        num = 0
        sqr = 0
        while sqr <= c:
            sqr = num**2
            sqr_set.add(sqr)
            if (c - sqr) in sqr_set:
                return True
            num += 1
        return False

        