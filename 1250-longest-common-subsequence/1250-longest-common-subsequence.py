class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def find_lcs_from_indexes(i: int, j: int):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if text1[i] == text2[j]:
                return find_lcs_from_indexes(i + 1, j + 1) + 1
            else:
                skip_left = find_lcs_from_indexes(i + 1, j)
                skip_right = find_lcs_from_indexes(i, j + 1)
                skip_both = find_lcs_from_indexes(i + 1, j + 1)
                return max(skip_left, skip_both, skip_right)
        
        return find_lcs_from_indexes(0, 0)