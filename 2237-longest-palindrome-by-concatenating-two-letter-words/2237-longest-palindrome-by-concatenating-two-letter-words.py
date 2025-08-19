class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        word_ct = collections.Counter(words)
        found_middle = False
        result_size = 0

        for word in list(word_ct.keys()):
            count = word_ct[word]
  
            if word[0] == word[1]:
                result_size += (count // 2) * 4

                if count % 2 == 1:
                    found_middle = True
            else:
                reverse = word[::-1]
                reverse_count = word_ct[reverse] 
                pair_count = min(reverse_count, count)
                result_size += pair_count * 4
                word_ct[reverse] -= pair_count
                word_ct[word] -= pair_count

        
        if found_middle:
            result_size += 2
        
        return result_size
