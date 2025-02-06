"""
Reverse a singly linked list given its head."""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_vals = []
        next = head.next
        node_vals.append(head.val)
        while next is not None:
            node_vals.append(next.val)
            next = next.next
        reversed_vals = node_vals[::-1]
        current = head
        for num in reversed_vals:
            current.val = num
            current = current.next
        return head



        