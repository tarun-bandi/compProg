"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
  def flatten(self, head):
    head_copy = head
    while head != None:
      if head.child != None:
        flattened_child = self.flatten(head.child)
        temp = head.next
        head.next = flattened_child
        flattened_child.prev = head
        while flattened_child.next != None:
          flattened_child = flattened_child.next
        flattened_child.next = temp
        if temp:
          temp.prev = flattened_child
        head.child = None

      head = head.next
      
    return head_copy
        