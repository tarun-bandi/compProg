class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        curr_openrooms = 0
        max_rooms = 0

        res = []

        for start, end in intervals:
            res.append((start, 1))
            res.append((end, 0))
        res.sort()

        for _, event in res:
            if event == 0:
                curr_openrooms -= 1
            else:
                curr_openrooms += 1
                max_rooms = max(curr_openrooms, max_rooms)

        return max_rooms


        