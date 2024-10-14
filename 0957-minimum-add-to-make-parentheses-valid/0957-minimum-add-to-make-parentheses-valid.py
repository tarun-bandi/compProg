class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #Invalid if 2 cases:
        #1: closed with no open. #2. open w/ no resulting close (end)

        added = 0
        open_ct = 0
        for c in s:
            if c == "(":
                open_ct += 1
            else:
                open_ct -= 1
                if open_ct < 0:
                    open_ct = 0
                    added += 1
        
        return added + open_ct
