class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        m = len(mat1)
        n = len(mat2[0])
        k = len(mat2)

        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                for l in range(k):
                    print(i, j, l)
                    print(n, m, k)
                    res[j][i] += mat1[j][l] * mat2[l][i]
            
        return res


        