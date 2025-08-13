class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        """
        Observations:
        We want to find "Pairs" - essentially (cl, lc) are a pair. We also want to find "middle" elements which are the same 2 characters
        """

        # We only can include one middle element

        middle_element_found = False
        seen = dict()
        pairs = 0 
        words.sort()
        print(words)
        for word in words:
            
            if word not in seen or seen[word] == 0:
                seen[word[::-1]] = seen.get(word[::-1], 0) +  1
            else:
                print(f"Pair: {word} and {word[::-1]}")
                seen[word] -= 1
                pairs += 4
            
        for word in seen:
            if seen[word] > 0 and word[0] == word[1]:
                middle_element_found = True
                break
        
        return pairs + (2 if middle_element_found else 0)

            

        