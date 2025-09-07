class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
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
