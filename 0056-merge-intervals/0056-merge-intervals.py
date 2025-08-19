class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        prev_interval = None

        results = []

        for (start, end) in intervals:
            if not prev_interval:
                prev_interval = [start, end]
            elif prev_interval[1] >= start:
                prev_interval = [prev_interval[0], max(end, prev_interval[1])]
            else:
                results.append(prev_interval)
                prev_interval = [start, end]
        
        if prev_interval:
            results.append(prev_interval)
        
        return results