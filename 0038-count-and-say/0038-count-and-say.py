class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(number: str):
            i = 0
            prev = ""
            count = 0
            res = ""
            while i < len(number):
                if number[i] == prev:
                    count += 1
                else:
                    if count != 0:
                        res += str(count)
                    res += prev
                    prev = number[i]
                    count = 1
                i += 1
            res += str(count)
            res += prev
            return res
        def dfs(n):
            if n == 1:
                return "1"
            else:
                return rle(dfs(n - 1))
        return dfs(n)
        