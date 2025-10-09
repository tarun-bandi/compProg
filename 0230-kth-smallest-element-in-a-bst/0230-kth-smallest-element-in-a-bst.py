# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compute_tree_sizes(self, node, tree_sizes):
        if node == None:
            return 0
        tree_sizes[node] = (self.compute_tree_sizes(node.left, tree_sizes)
        + self.compute_tree_sizes(node.right, tree_sizes) + 1)
        return tree_sizes[node]
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree_sizes = dict()
        tree_sizes[None] = 0

        def inner(root, k):
            if root == None:
                return -1
            self.compute_tree_sizes(root, tree_sizes)

            lhs_size = tree_sizes[root.left]
            if lhs_size + 1 == k:
                return root.val
            if lhs_size + 1 > k:
                return inner(root.left, k)
            else:
                return inner(root.right, k - lhs_size - 1)
        
        return inner(root, k)