class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s) : True}

        for i in range(len(s) - 1, -1, -1):
            
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    if i + len(w) in dp and dp[i + len(w)]:
                        dp[i] = True
            if i not in dp:
                dp[i] = False
        
        return dp[0]


        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]

            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                     s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)