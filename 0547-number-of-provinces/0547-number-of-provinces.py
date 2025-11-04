class UF:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return 0

        if self.size[root_u] > self.size[root_v]:
            self.size[root_u] += self.size[root_v]
            self.parents[root_v] = root_u
        else:
            self.size[root_v] += self.size[root_u]
            self.parents[root_u] = root_v
        
        return 1
    def find(self, u):
        
        while u != self.parents[u]:
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
        
        return u

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        union_find = UF(n)
        cc = n 
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    cc -= union_find.union(i, j)
        
        return cc
                
        