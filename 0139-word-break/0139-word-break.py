class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[n][n] = True
        for i in range(n):
            dp[i][n] = False

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                take = False
                curr_string = s[i: j + 1]
                if curr_string in wordDict:
                    take = dp[j + 1][j + 1]
                not_take = dp[i][j + 1]
                dp[i][j] = take or not_take
        
        return dp[0][0]



        @cache
        def dp(i: int, j: int):
            if i >= len(s) and j >= len(s):
                return True
            if j >= len(s):
                return False
            sting = s[i:j + 1]
            take = False
            if sting in wordDict:
                take = dp(j + 1, j + 1)
            not_take = dp(i, j + 1)
            return take or not_take
        
        return dp(0, 0)