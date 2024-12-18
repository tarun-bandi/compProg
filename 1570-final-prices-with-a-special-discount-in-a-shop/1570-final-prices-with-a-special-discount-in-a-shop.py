class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        runningMin = float("inf")
        stack =[]
        res = []
        for c in prices[::-1]:
            if not stack:
                res.append(c)
                stack.append(c)
            else:
                while stack and stack[-1] > c:
                    stack.pop()
                if stack:
                    res.append(c - stack[-1])
                else:
                    res.append(c)
                stack.append(c)
        
        
        return res[::-1]
            