class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo = 0
        hi = position[-1]
        #be "greedy... loop thru positions and pick the first one that is atleast m gretaret than prev"

        def canSatisfyForce(min_distance : int) -> bool:
            prev = position[0]
            count = 1
            for c in position[1:]:
                if c - prev >= min_distance:
                    count += 1
                    prev = c
                    print(c, count)
                if count == m:
                    return True
            return False
        
        curr_max = 0
        while lo < hi:
            mid = (lo + hi)//2
            print("lo", lo, hi, curr_max)
            if canSatisfyForce(mid):
                curr_max = max(curr_max, mid)
                lo = mid + 1
            else:   
                hi = mid
        return curr_max




