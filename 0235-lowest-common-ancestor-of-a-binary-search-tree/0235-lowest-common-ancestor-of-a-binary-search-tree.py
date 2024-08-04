# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lower_value = min(p.val, q.val)
        higher_value = max(p.val, q.val)

        while root:
            if lower_value <= root.val <= higher_value:
                return root
            elif root.val < lower_value:
                root = root.right
            else:
                root = root.left
        return None
            
        

