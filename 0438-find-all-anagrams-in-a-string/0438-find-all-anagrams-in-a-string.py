class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        def char_to_index(char: str) -> int:
            """ Uses ord to convert lowercase char to place in alphabet """
            return ord(char) - ord('a')

        anagram_list = []
        s_counts = [0] * 26
        p_counts = [0] * 26

        for index in range(len(p)):

            p_counts[char_to_index(p[index])] += 1
            s_counts[char_to_index(s[index])] += 1
        
        indeces = []
        for index in range(len(p), len(s)):
            if s_counts == p_counts:
                indeces.append(index - len(p))

            s_counts[char_to_index(s[index - len(p)])] -= 1
            s_counts[char_to_index(s[index])] += 1
            index += 1
        if s_counts == p_counts:
            indeces.append(len(s) - len(p))
        
        return indeces

        





        