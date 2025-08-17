class Solution:
    def myAtoi(self, s: str) -> int:
        import re
        match = re.match(r' *([+-]?\d+)', s)
        num = int(match.group(1)) if match else 0
        return max(min(num, 2**31 - 1), -2**31)
