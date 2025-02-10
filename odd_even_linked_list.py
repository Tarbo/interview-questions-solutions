"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity."""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        odd_list = head
        even_list = head.next
        even_head = even_list
        current_node = even_list.next
        index = 3
        while current_node is not None:
            if index % 2 == 0:
                even_list.next = current_node
                even_list = even_list.next
            else:
                odd_list.next = current_node
                odd_list.next = odd_list.next
            index += 1
            current_node = current_node.next
        odd_list.next = even_head
        even_list.head = None
        return head
        