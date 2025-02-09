"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively."""
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_nodes = 1
        # find the number of nodes
        current = head.next
        while current is not None:
            num_nodes += 1
            current = current.next
        target_node = num_nodes // 2
        if num_nodes == 1:
            return None
        current = head
        previous = head
        i = 0
        for i in range(num_nodes):
            if i == target_node:
                previous.next = current.next
                current.next = None
            else:
                previous = current
                current = current.next
                i += 1
        return head

