class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rowInds, colInds = [], []
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowInds.append(r)
        for c in range(cols):
            for r in range(rows):
                if grid[r][c] == 1:
                    colInds.append(c)
        
        row = rowInds[len(rowInds) // 2]
        col = colInds[len(colInds) // 2]

        def minDist1D(points, origin):
            dist = 0
            for point in points:
                dist += abs(point - origin)
            return dist
        
        return minDist1D(rowInds, row) + minDist1D(colInds, col)