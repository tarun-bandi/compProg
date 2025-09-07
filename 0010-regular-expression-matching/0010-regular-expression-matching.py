class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            print(i, j)
            if i < 0 and j < 0:
                return True
            if j < 0:
                return False
            if i < 0:
                if p[j] == '*':
                    return dp(i, j - 2)
                return False

            is_possible = False
            if s[i] == p[j] or p[j] == '.':
                is_possible |= dp(i - 1, j - 1)
            if p[j] == '*':
                regex_char = p[j - 1]
                if s[i] == regex_char or regex_char == '.':
                    is_possible |= dp(i - 1, j)
                    is_possible |= dp(i - 1, j - 2)
                is_possible |= dp(i, j - 2)
            return is_possible
        
        return dp(len(s) - 1, len(p) - 1)