class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
        Let's use a 2 pointer approach and keep counters. 
        """

        character_count = [0 for _ in range(26)]

        l = 0

        longest_replacable = 0

        def char_to_index(character):
            return ord(character) - ord("A")
        
        def substring_is_invalid():
            return sum(character_count) - max(character_count) > k

        for r in range(len(s)):
            character_count[char_to_index(s[r])] += 1
            while substring_is_invalid():
                character_count[char_to_index(s[l])] -= 1
                l += 1
            longest_replacable = max(longest_replacable, r - l + 1)
        
        return longest_replacable



        