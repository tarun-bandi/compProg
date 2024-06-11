class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counted = Counter(arr1)

        arr_1set = set(arr1)
        res = []
        for c in arr2:
            for _ in range(counted[c]):
                res.append(c)
            arr_1set.remove(c)
        for c in sorted(list(arr_1set)):
            for _ in range(counted[c]):
                res.append(c)
        return res


