class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
            else:
                carry = 0
                break
        if carry:
            digits = [1] + digits
        return digits
            
        