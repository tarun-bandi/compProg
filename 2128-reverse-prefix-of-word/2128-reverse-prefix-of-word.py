class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        build = ""

        for i,a in enumerate(word):
            build += a
            if a == ch:
                return build[::-1] + word[i + 1:]
        return build

