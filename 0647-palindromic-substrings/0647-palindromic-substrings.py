class Solution:
    def countSubstrings(self, s: str) -> int:

        @cache
        def is_palindrome(start_index : int, end_index : int) -> bool:
            if start_index == end_index: # ""
                return True
            if start_index + 1 == end_index: # Singleton
                return True
            return s[start_index] == s[end_index - 1] and is_palindrome(start_index + 1, end_index - 1)
        
        count = 0
        for i in range(len(s)):
            for j in range(1, len(s) + 1):
                if i < j and is_palindrome(i, j):
                    count += 1
        
        return count


            


            
                
        
        