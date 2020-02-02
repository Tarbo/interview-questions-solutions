"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, data):
        newNode = ListNode(data)
        if self.head is None:  # first data is inserted here
            self.head = newNode
            return
        next_node = self.head
        while next_node.next:
            next_node = next_node.next
        next_node.next = newNode

    def print_list(self):
        """print the list to test the accuracy of the code"""
        current_node = self.head
        while current_node is not None:
            print(current_node.val)
            current_node = current_node.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_values = []
        l2_values = []
        # append the fist numbers assuming non-empty linked list
        l1_values.append(l1.head.val)
        l2_values.append(l2.head.val)
        # traverse the l1
        l1_next = l1.head.next
        while l1_next is not None:
            l1_values.append(l1_next.val)
            l1_next = l1_next.next
        # traverse l2
        l2_next = l2.head.next
        while l2_next is not None:
            l2_values.append(l2_next.val)
            l2_next = l2_next.next
        # reverse the lists
        l1_values = l1_values[::-1]
        l2_values = l2_values[::-1]
        # join to form single number in case the dimensions are not the same
        l1_num = int("".join([str(num) for num in l1_values]))
        l2_num = int("".join([str(num) for num in l2_values]))
        # add the numbers
        sum_num = l1_num + l2_num
        # split the number for onward storage to a linked list
        num_list = [int(num) for num in str(sum_num)]
        # make a list of nodes
        list_of_listnodes = [ListNode(num) for num in num_list[::-1]]
        # chain the list nodes
        for idx in range(len(list_of_listnodes)-1):
            list_of_listnodes[idx].next = list_of_listnodes[idx+1]

            # call the Slinkedlist
            # return_list = SLinkedList()
            # for num in number_reversed_list:
            #     return_list.insert_at_end(num)
            # return_list.print_list()
        return list_of_listnodes[0]


if __name__ == "__main__":
    l1 = SLinkedList()
    l2 = SLinkedList()
    # l1.head = ListNode(2)
    # l1.head.next = ListNode(4)
    # l1.head.next.next = ListNode(3)
    data_1 = [2, 4, 3]
    data_2 = [5, 6, 4]
    for num in data_1:
        l1.insert_at_end(num)
    for num in data_2:
        l2.insert_at_end(num)
    # test the print function
    # l1.print_list()
    # l2.print_list()
    solution = Solution()
    solution.addTwoNumbers(l1, l2)
