class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def find_matches_from_index(i: int, j: int):
            
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < len(p) and p[j + 1] == '*':
                dont_use = find_matches_from_index(i, j + 2)
                use = match and find_matches_from_index(i + 1, j)
                return use or dont_use
            
            if match:
                return find_matches_from_index(i + 1, j + 1)
            
            return False
        
        return find_matches_from_index(0, 0)