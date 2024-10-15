class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def cando(mid):
            day = 0
            weight = 0
            for c in weights:
                weight += c
                if weight > mid:
                    day += 1
                    weight = c
            if weight > 0:
                day += 1
            return day <= days



        lo = max(weights)
        high = sum(weights) + 1

        while lo < high:
            mid = (lo + high)//2
            if cando(mid):
                high = mid
            else:
                lo = mid + 1
        
        return high