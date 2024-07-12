class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        rm = ""
        other = ""
        if x > y:
            rm = "ab"
            other = "ba"
        else:
            rm = "ba"
            other = "ab"
        stack.append(s[0])
        score = 0
        for c in s[1:]:
            if stack and stack[-1] + c == rm:
                score += max(x, y)
                stack.pop()
            else:
                stack.append(c)
        s = "".join(stack)
        stack = []
        for c in s:
            if stack and stack[-1] + c == other:
                score += min(x, y)
                stack.pop()   
            else:
                stack.append(c)
        return score   
        
        


            


        