class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        deleted = True
        def is_palindrome(l, r):
            return s[l:r] == s[l:r][::-1]
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -=1
            else:
                return is_palindrome(l, r) or is_palindrome(l + 1, r + 1)
        return True
            
