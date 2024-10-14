class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []
        curr = intervals[0]
        for x, y in intervals[1:]:

            if curr[1] >= x: 
                curr = [min(curr[0], x), max(curr[1], y)]
            else:
                result.append(curr)
                curr = [x, y]
        result.append(curr)
        return result
                

