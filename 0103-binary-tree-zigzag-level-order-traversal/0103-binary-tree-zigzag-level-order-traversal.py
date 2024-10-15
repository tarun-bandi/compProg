# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = defaultdict(list)

        queue = deque([(0, root)])
        longest_level = 0
        while queue:
            lvl, node = queue.popleft()
            if node:
                longest_level = lvl
                results[lvl].append(node.val)
                queue.append((lvl + 1, node.left))
                queue.append((lvl + 1, node.right))
        
        res = []
        for r in range(longest_level + 1):
            if results[r]:
                if r % 2 == 0:
                    res.append(results[r])
                else:
                    res.append(results[r][::-1])
        return res
            

        