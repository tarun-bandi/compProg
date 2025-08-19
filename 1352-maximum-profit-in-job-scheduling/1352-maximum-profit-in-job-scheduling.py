class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        events = sorted(zip(startTime, endTime, profit))
        

        @cache
        def dp(time: int) -> int:
            if time == len(events):
                return 0
                
            start, end, profit = events[time]
            next_event_idx = bisect.bisect_left(events, (end, 0, 0))

            return max(profit + dp(next_event_idx), dp(time + 1))
        
        return dp(0)

