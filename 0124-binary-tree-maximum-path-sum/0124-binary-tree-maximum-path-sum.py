# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.largestSeen = float("-inf")
        def getLargest(root):
            if not root:
                return float("-inf")
            largest = float("-inf")
            left = getLargest(root.left)
            right = getLargest(root.right)
            largest = max(left + root.val, right + root.val, root.val)
            self.largestSeen = max(left, right, largest, self.largestSeen, left + right + root.val)

            return largest
        getLargest(root)
        return self.largestSeen