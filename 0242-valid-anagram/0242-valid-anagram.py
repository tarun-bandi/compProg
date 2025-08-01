class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = collections.Counter(s)
        counts_t = collections.Counter(t)

        if (len(counts_s) != len(counts_t)):
            return False
        for letter in counts_t:
            if counts_t[letter] != counts_s.get(letter, 0):
                return False
        
        return True