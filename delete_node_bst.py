"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delete(self, node: Optional[TreeNode], key: int, parent_node: Optional[TreeNode])-> Optional[TreeNode]:
        if node is None:
            return None
        if node.val < key:
            parent_node = node
            return self.delete(node.right, key, parent_node)
        elif node.val > key:
            parent_node = node
            return self.delete(node.right, key, parent_node)
        else: #key found
            # leaf node deletion
            if node.right == node.left == None and parent_node.left.val == key:
                parent_node.left = None
            elif node.right == node.left == None and parent_node.right.val == key:
                parent_node.right = None
            # one child
            elif node.right is not None and node.left is None and parent_node.left.val == key:
                parent_node.left = node.right
            elif node.right is None and node.left is not None and parent_node.right.val == key:
                parent_node.right = node.left
            # two children
            elif parent_node.left.val == key:
                parent_node.left = node.left
                parent_node.left.right = node.right
            else:
                parent_node.right = node.left
                parent_node.left.right = node.right



    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
       
            

