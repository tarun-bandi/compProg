class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def find_edit_distance_from_indexes(i: int, j: int):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            distance = find_edit_distance_from_indexes(i + 1, j + 1)

            if word1[i] != word2[j]:
                distance += 1
            
            distance = min(distance, 1 + find_edit_distance_from_indexes(i + 1, j))
            distance = min(distance, 1 + find_edit_distance_from_indexes(i, j + 1))
            return distance
        
        return find_edit_distance_from_indexes(0, 0)
                