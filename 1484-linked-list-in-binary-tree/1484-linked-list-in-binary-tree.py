# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(listPtr, treePtr, atStart):
            if (listPtr) == None:
                return True
            if treePtr == None:
                return False
            if listPtr.val != treePtr.val and not atStart:
                return False
            if (atStart and listPtr.val != treePtr.val):
                return dfs(listPtr, treePtr.left, atStart) or dfs(listPtr, treePtr.right, atStart)
            elif atStart:
                return dfs(listPtr, treePtr.left, atStart) or dfs(listPtr, treePtr.right, atStart) or dfs(listPtr.next, treePtr.left, False) or dfs(listPtr.next, treePtr.right, False)

            return dfs(listPtr.next, treePtr.left, False) or dfs(listPtr.next, treePtr.right, False)
        return dfs(head, root, True)

