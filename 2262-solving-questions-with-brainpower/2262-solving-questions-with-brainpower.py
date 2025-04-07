class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        

        #Dynamic programming problem - consider every choice and take the maximum

        #Pick/don't pick

        @cache
        def dp(i : int) -> int:
            if i >= len(questions): return 0

            points, skips = questions[i]

            return max(points + dp(i + skips + 1), dp(i + 1))

        return dp(0)

