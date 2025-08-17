# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = dict()
        start_node = None
        end_node = None

        def dfs(node):
            nonlocal start_node
            nonlocal end_node 
            if node == None:
                return
            parents[node.left] = node
            parents[node.right] = node
            
            if node.val == startValue:
                start_node = node
            if node.val == destValue:
                end_node = node
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        if start_node == None or end_node == None:
            return ""

        queue = collections.deque()
        queue.append((start_node, ""))
        seen = {None}

        while queue:
            current_node, path = queue.popleft()
            if current_node in seen:
                continue
            seen.add(current_node)
            
            if current_node == end_node:
                return path
            
            if current_node in parents:
                queue.append((parents[current_node], path + "U"))
            
            if current_node.left not in seen:
                 queue.append((current_node.left, path + "L"))
            if current_node.right not in seen:
                queue.append((current_node.right, path + "R"))
        
        return ""
            
                        
            

