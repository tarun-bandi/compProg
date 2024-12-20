# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1copy = l1
        l2copy = l2
        carry = 0
        dummy = None
        prev = None
        while l1 and l2:
            res = ListNode()
            if not dummy:
                dummy = ListNode()
                dummy.next = res

            res.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry)//10
            if prev:
                prev.next = res
            prev = res
            l1 = l1.next
            l2 = l2.next

        while l1:
            res = ListNode()
            res.val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            prev.next = res
            prev = res
            l1 = l1.next
        while l2:
            res = ListNode()
            res.val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            prev.next = res
            prev = res
            l2 = l2.next
        if carry != 0:
            res = ListNode()
            res.val = carry
            prev.next = res
        return dummy.next

