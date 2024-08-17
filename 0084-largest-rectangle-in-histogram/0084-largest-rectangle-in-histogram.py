class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        largest_area = 0
        for i, h in enumerate(heights):
            if not stack:
                stack.append((h, 0))
            else:
                last_removed = (0, i)
                while stack and h < stack[-1][0]:
                    last_removed = stack.pop()
                    largest_area = max(largest_area, (i - last_removed[1]) * last_removed[0])

                stack.append((h, last_removed[1]))

        while stack:
            height, start = stack.pop()
            largest_area = max(height * (len(heights) - start), largest_area)
        return largest_area

