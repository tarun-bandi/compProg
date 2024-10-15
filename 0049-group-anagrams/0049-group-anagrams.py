class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordGroups = defaultdict(list)
        for word in strs:
            key = [0] * 26

            for c in word:
                key[ord(c) - ord('a')] += 1
            wordGroups[tuple(key)].append(word)

        res = []
        for key in wordGroups:
            res.append(wordGroups[key])
        return res
