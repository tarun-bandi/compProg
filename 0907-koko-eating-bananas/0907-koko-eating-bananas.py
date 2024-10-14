class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def can_eat(speed, h):

            time = 0

            for pile in piles:
                time += math.ceil(pile/speed)
                if time > h:
                    return False
            return time <= h
        

        lo = 1
        hi = max(piles) #O(n)

        while lo < hi:
            mid = (lo + hi) // 2
            if can_eat(mid, h):
                hi = mid 
            else:
                lo = mid + 1
        
        return hi