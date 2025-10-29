class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        previous_mappings = dict()
        seen_words = set()

        if len(pattern) != len(words):
            return False

        for character, word in zip(pattern, words):
            if character in previous_mappings and previous_mappings[character] != word:
                return False
            elif character not in previous_mappings and word in seen_words:
                return False
            
            seen_words.add(word)
            
            previous_mappings[character] = word

        return True
