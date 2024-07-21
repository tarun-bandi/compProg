class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = -1
        for a, b in edges:
            n = max(n, a, b)
        for i, (x, y) in enumerate(edges):
            edges[i] = [x - 1, y - 1]
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(node):
            
            res = node

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(node, node2):
            par, par2 = find(node), find(node2)
            if par == par2:
                return 0
            else:
                if rank[par] > rank[par2]:
                    rank[par] += rank[par2]
                    parent[par2] = par
                else:
                    rank[par2] += rank[par]
                    parent[par] = par2
            return 1
        for a, b in edges:
            union_status = union(a, b)
            if union_status == 0:
                return [a + 1, b + 1]
            print(union_status)
        return []

        