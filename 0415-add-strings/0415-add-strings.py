class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        carry = 0

        while i >= 0 or j >= 0:
            curr = carry

            if i >= 0:
                curr += int(num1[i])
            if j >= 0:
                curr += int(num2[j])
            res += str(curr % 10)
            carry = curr//10

            i = max(i - 1 ,-1)
            j = max(j - 1, -1)

        if carry:
            res += str(carry)
        
        return res[::-1]