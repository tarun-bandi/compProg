# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def tree_to_list(tree):
            if tree == None:
                return []
            else:
                left = tree_to_list(tree.left)
                mid = [tree.val]
                right = tree_to_list(tree.right)
                return left + mid + right
        
        this_tree = tree_to_list(root)
        def list_to_tree(array):
            if array == []:
                return None
            else:
                mid = len(array)//2
                left = list_to_tree(array[:mid])
                right = list_to_tree(array[mid+1:])
                return TreeNode(array[mid], left, right)
        return list_to_tree(this_tree)
        