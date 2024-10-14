# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = dict()
        def dfs(node, parent):
            graph[node] = [node.left, node.right, parent]
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        
        dfs(root, None)
        queue = collections.deque()
        queue.append((target, 0))
        result = []
        seen = set()
        while queue:
            node, dist = queue.popleft()
            if node in seen or not node:
                continue
            seen.add(node)
            if dist == k:
                result.append(node.val)
            elif node:
                for c in graph[node]:
                    queue.append((c, dist + 1))
        
        return result




