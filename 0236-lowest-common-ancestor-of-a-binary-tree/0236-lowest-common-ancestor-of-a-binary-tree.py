# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = dict()

        queue = collections.deque()
        queue.append((None, root))

        while queue:
            par, node = queue.popleft()

            if node:
                parent[node] = par
                queue.append((node, node.left))
                queue.append((node, node.right))
        
        pcopy, qcopy = p, q
        while pcopy != qcopy:
            pcopy = parent[pcopy] if pcopy else q
            qcopy = parent[qcopy] if qcopy else p
        return pcopy


