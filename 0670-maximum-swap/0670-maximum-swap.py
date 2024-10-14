class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        ordered = sorted(num, reverse=True)
        unEq = 0
        for i in range(len(num)):
            if num[i] != ordered[i]:
                for j in range(len(num) - 1, i - 1, -1):
                    if num[j] == ordered[i]:
                        unEq = j
                        break
                num[i], num[j] = num[j], num[i]
                return int("".join(num))
        return int("".join(num))




        