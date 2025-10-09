class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""


        for j in range(min(len(word1), len(word2))):
            res += word1[j]
            res += word2[j]
        j += 1
        while j < len(word2):
            res += word2[j]
            j+=1
        
        while j < len(word1):
            res += word1[j]
            j += 1
        
        return res