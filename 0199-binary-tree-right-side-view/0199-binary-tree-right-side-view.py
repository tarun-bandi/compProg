# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #just do bfs and output rightmost node by giving each node some kinda rank......

        q = collections.deque()
        q.append((root, 0))
        if root == None:
            return None
        res = []
        while q:
            highest = float("-inf")
            maxNode = None
            copy = collections.deque()
            while q:
                node, lvl = q.popleft()
                maxNode = node
                if node.left != None:
                    copy.append((node.left, lvl - 1))
                if node.right != None:
                    copy.append((node.right, lvl + 1))
            q = copy
            res.append(maxNode.val)
        return res

                
                

        