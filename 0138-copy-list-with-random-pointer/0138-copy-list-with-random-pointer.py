"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        headcopy = head
        oldToNew = dict()
        oldToNew[None] = None
        while headcopy:
            oldToNew[headcopy] = Node(headcopy.val)
            headcopy = headcopy.next
        
        headcopy = head
        while headcopy:
            new = oldToNew[headcopy]
            nextNode = oldToNew[headcopy.next]
            randomNode = oldToNew[headcopy.random]
            new.next = nextNode
            new.random = randomNode
            headcopy = headcopy.next
        
        return oldToNew[head]

