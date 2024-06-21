class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        l = 0
        r = minutes
        max_delta = 0
        for c in range(r):
            if grumpy[c] == 1:
                max_delta += customers[c]
        cur_delta = max_delta
        while r < len(customers):
            print(cur_delta, r)
            if grumpy[l] == 1:
                cur_delta -= customers[l]
            l += 1
            if grumpy[r] == 1:
                cur_delta += customers[r]
            max_delta = max(cur_delta, max_delta)
            r += 1

        normal = 0
        for c in range(len(customers)):
            grumpy[c] = 1 if grumpy[c] == 0 else 0
            normal += customers[c] * (grumpy[c])

        
        return max_delta + normal

                


        