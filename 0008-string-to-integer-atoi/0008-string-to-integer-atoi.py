class Solution:
    def myAtoi(self, s: str) -> int:

        if s == "":
            return 0
        index = 0

        while index < len(s) and s[index] == " ":
            index += 1
        if index == len(s):
            return 0
        negative = False
        if s[index] == "-":
            negative = True
            index += 1
        elif s[index] == "+":
            index += 1

        result = 0
        if index == len(s):
            return 0
            
        def rounded(num: int) -> int:
            if num < - 2 ** 31:
                return -(2 ** 31)
            elif num >= 2 ** 31 - 1:
                return 2 ** 31 - 1
            return num
        
        while index < len(s):
            if not s[index].isdigit():
                return rounded(result * (-1 if negative else 1))
            
            result *= 10
            result += int(s[index])
            index += 1
        return rounded(result * (-1 if negative else 1))

            
        