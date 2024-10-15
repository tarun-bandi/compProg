# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        results = defaultdict(list)

        queue = deque([root])
        longest_level = 0
        right = True
        if not root:
            return []
        while queue:
            lev = []
            for _ in range(len(queue)):
                if right:
                    node = queue.popleft()
                    lev.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    lev.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            right = not right
            res.append(lev)

        return res
            

        