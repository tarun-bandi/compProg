class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        degrees = dict()

        for (x, y) in roads:
            degrees[x] = degrees.get(x, 0) + 1
            degrees[y] = degrees.get(y, 0) + 1

        values = list(degrees.values())
        values.sort(reverse=True)
        
        total = 0
        curr = n
        for v in values:
            total += v * curr
            curr -= 1
        return total
        