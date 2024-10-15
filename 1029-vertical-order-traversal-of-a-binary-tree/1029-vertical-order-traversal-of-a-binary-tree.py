# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = collections.deque()

        q.append((root, 0, 0))
        seen = set()
        columnToNodes = collections.defaultdict(list)
        left = float('inf')
        right = float('-inf')
        while q:
            curr, x, y = q.popleft()
            left = min(left, y)
            right = max(right, y)
            if curr.left:
                q.append((curr.left, x + 1, y - 1))
            if curr.right:
                q.append((curr.right, x + 1, y + 1))
            columnToNodes[y].append((x, curr.val))
        
        res = []
        for c in range(left, right + 1):
            cur = []
            columnToNodes[c].sort()
            for c in columnToNodes[c]:
                _, val = c
                cur.append(val)
            res.append(cur)
        return res





