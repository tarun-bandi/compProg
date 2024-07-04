# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_sum = 0
        last_zero = None
        fst = last_zero
        while head != None:
            if head.val == 0 and curr_sum != 0:
                if last_zero == None:
                    last_zero = ListNode(val=curr_sum, next=None)
                    fst = last_zero
                else:
                    last_zero.next = ListNode(val=curr_sum, next=None)
                    last_zero = last_zero.next
                curr_sum = 0
            print(head.val)
            curr_sum += head.val
            head = head.next
        return fst





        