class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        seats.sort()
        students.sort()
        dist = 0
        for x,y in zip(seats, students):
            dist += abs(x - y)
        return dist

        