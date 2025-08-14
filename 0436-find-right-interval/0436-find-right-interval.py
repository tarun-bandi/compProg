class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        indexed_intervals = [(f[0], i) for (i, f) in enumerate(intervals)]
        indexed_intervals.sort()
        indexes = [i for (_, i) in indexed_intervals]
        sorted_start_times = [x for (x, _) in indexed_intervals]

        results = []
        for _, y in intervals:
            insertion_index = bisect.bisect_left(sorted_start_times, y)
            results.append(indexes[insertion_index] if insertion_index < len(indexes) else -1)
        
        return results

