class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        

        #Dynamic programming problem - consider every choice and take the maximum

        #Pick/don't pick
        dp = [0 for _ in range(len(questions))]

        for i in range(len(questions) - 1, -1, -1):
            points, power = questions[i]
            if i + power + 1 >= len(questions):
                dp[i] = points
            else:
                dp[i] = points + dp[i + power + 1]
            if i < len(questions) - 1:
                dp[i] = max(dp[i + 1], dp[i])
        return dp[0]
        @cache
        def dp(i : int) -> int:
            if i >= len(questions): return 0

            points, skips = questions[i]

            return max(points + dp(i + skips + 1), dp(i + 1))

        return dp(0)

