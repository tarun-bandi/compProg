class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] 
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack or stack[-1][1] >= t: 
                stack.append((i, t))
            else:
                while stack and stack[-1][1] < t: 
                    index, _ = stack.pop()
                    result[index] = i - index
                stack.append((i, t))
        return result
