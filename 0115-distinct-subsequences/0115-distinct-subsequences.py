class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def count_num_distinct(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            counts = 0
            if s[i] == t[j]:
                counts += count_num_distinct(i + 1, j + 1)

            skip_left = count_num_distinct(i + 1, j)
            counts += skip_left

            return counts
        return count_num_distinct(0, 0)
