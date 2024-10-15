class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        results = [0] * n

        # ["0:start:0","1:start:2","1:end:5","0:end:6"]
        # CallStack = []
        # [("0:start:0"), ("1:start:2")]
        #[("5:start:0")]

        stack = []
        for log in logs:
            function, callType, currTime = log.split(":")
            function = int(function)
            currTime = int(currTime)
            if callType == "start":
                if stack:
                    prevFunc, prevTime = stack[-1]
                    print(prevTime, currTime)
                    results[prevFunc] += currTime - prevTime #CHECK FOR OBO
                stack.append((function, currTime))
            else:
                func, end = stack.pop()
                results[func] += currTime - end+ 1
                if stack:
                    prevFunc, prevTime = stack[-1]
                    stack[-1] = (prevFunc, currTime + 1)
        return results



