class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def count_number_of_decodings_from(i: int) -> int:
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s) - 1:
                return 1
            next_two = int(s[i:i+2])
            ways = count_number_of_decodings_from(i + 1)
            if 10 <= next_two <= 26:
                ways += count_number_of_decodings_from(i + 2)
            
            return ways
        
        return count_number_of_decodings_from(0)
                


        