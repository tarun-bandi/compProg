class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        number_of_decodings_from2 = 1
        number_of_decodings_from1 = 1 if s[n - 1] != '0' else 0

        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                number_of_decodings_from2 = number_of_decodings_from1
                number_of_decodings_from1 = 0
                continue

            next_2 = int(s[i:i + 2])
            ways = number_of_decodings_from1
            if 10 <= next_2 <= 26:
                ways += number_of_decodings_from2
            number_of_decodings_from2 = number_of_decodings_from1
            number_of_decodings_from1 = ways
        return number_of_decodings_from1
            

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
                


        