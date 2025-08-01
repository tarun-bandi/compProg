"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_to_clone = dict()
        if node == None:
            return None 
        def dfs(node):
            if node in node_to_clone:
                return
            
            clone = Node(val = node.val)
            node_to_clone[node] = clone

            for neighbor in node.neighbors:
                dfs(neighbor)
            
            clone.neighbors = [node_to_clone[neighbor] for neighbor in node.neighbors]


        dfs(node)
        return node_to_clone[node]
            
        