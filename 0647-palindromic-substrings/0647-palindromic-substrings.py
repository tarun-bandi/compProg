class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        @cache
        def is_palindrome(i, j):
            if i > j:
                return True
            return s[i] == s[j] and is_palindrome(i + 1, j - 1)

        count = 0
        for i in range(0, n):
            for j in range(i, n):
                count += 1 if is_palindrome(i, j) else 0

        return count
