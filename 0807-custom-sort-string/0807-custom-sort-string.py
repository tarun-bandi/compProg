class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        counter = Counter(s)
        res = ""
        for c in order:
            res += c * counter[c]
            del counter[c]
        
        for c in counter:
            res += c * counter[c]
        
        return res
