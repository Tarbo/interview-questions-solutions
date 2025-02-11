"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list_vals = []
        node_pointer = head
        while node_pointer is not None:
            list_vals.append(node_pointer.val)
            node_pointer = node_pointer.next
        num = len(list_vals)
        length = num//2
        pair_sum_list = [0] * length
        for i in range(length):
            pair_sum_list[i] = list_vals[i] + list_vals[num-1-i]
        return max(pair_sum_list)
    
