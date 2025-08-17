class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        
        anagram_list = []
        string_counts = [0] * 26
        pattern_counts = [0] * 26

        def char_to_index(char: str) -> int:
            """ Uses ord to convert lowercase char to place in alphabet """
            return ord(char) - ord('a')
        
        def pattern_equal_counts(string_cts, pattern_cts):
            for i in range(26):
                if string_cts[i] != pattern_cts[i]:
                    return False
            return True

        index = 0

        while index < len(p):
            pattern_char = p[index]
            string_char = s[index]

            pattern_counts[char_to_index(pattern_char)] += 1
            string_counts[char_to_index(string_char)] += 1
        
            index += 1
        indeces = []
        while index <= len(s):
            print(index - len(p), pattern_counts)
            if pattern_equal_counts(string_counts, pattern_counts):
                indeces.append(index - len(p))
            
            removing_character = s[index - len(p)]
            adding_character = s[index] if index < len(s) else "a"
            string_counts[char_to_index(removing_character)] -= 1
            string_counts[char_to_index(adding_character)] += 1
            index += 1
        
        return indeces

        





        