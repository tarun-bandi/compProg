class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        p1 = p2 = 0

        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            s1, f1 = firstList[p1]
            s2, f2 = secondList[p2]
            if f1 < s2:
                p1 += 1
            elif f2 < s1:
                p2 += 1
            else:
                res.append([max(s1, s2), min(f1, f2)])
                if f1 > f2:
                    p2 += 1
                else:
                    p1 += 1
        return res
