class Solution:
    def myAtoi(self, s: str) -> int:

        index = 0
        while index < len(s) and s[index] == " ":
            index += 1

        if index == len(s):
            return 0
        
        negative = False
        if s[index] in "+-":
            negative = s[index] == "-"
            index += 1
        
        number = 0
        while index < len(s):
            if s[index].isdigit():
                number *= 10
                number += int(s[index])
                index += 1
            else:
                break
        if negative:
            number *= -1
        return max(min(number, 2 ** 31 - 1), - 2**31)
