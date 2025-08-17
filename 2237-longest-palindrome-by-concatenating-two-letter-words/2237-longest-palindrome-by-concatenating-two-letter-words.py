class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        word_counter = collections.defaultdict(int)
        palindome_size = 0
        for word in words:

            if word[::-1] in word_counter:
                word_counter[word[::-1]] -= 1

                if word_counter[word[::-1]] == 0:
                    del word_counter[word[::-1]]
                palindome_size += 4
            else:
                word_counter[word] += 1
        
        for word in word_counter:
            if word[0] == word[1]:
                palindome_size += 2
                break
        
        return palindome_size

