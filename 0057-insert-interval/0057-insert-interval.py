class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for i, (x, y) in enumerate(intervals):
            if newInterval[1] < x:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif newInterval[0] > y:
                res.append([x, y])
            else:
                newInterval = [min(newInterval[0], x), max(newInterval[1], y)]
            
        return res




