class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        if intervals == []:
            return True
        prev_end = intervals[0][1]

        for x, y in intervals[1:]:
            if x < prev_end:
                return False
            prev_end = y

        return True