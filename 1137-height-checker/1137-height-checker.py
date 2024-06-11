class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #start 9:35:50

        expected = sorted(heights)
        ct = 0
        for x, y in zip(heights, expected):
            ct += 1 if x != y else 0
        return ct

