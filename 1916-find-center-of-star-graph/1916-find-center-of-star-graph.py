class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[1][1] if edges[1][1] in edges[0] else edges[1][0]