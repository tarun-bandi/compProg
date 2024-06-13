class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        currSize = 0
        boat_ct = 0
        curr_boat = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            print(left,right)
            if people[right] + people[left] > limit:
                right -= 1
            else:
                right -= 1
                left += 1
            boat_ct += 1
        return boat_ct

                
        