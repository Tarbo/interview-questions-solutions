"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

"""
class Solution:
    def generate_leaves(self, node:Optional[TreeNode], leaves: List[int])->None:
        if node is None:
            return
        if node.left == node.right == None:
            leaves.append(node.val)
        self.generate_leaves(node.left, leaves)
        self.generate_leaves(node.right, leaves)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None or root2 is None:
            return False
        leaves_1 = []
        self.generate_leaves(root1, leaves_1)
        leaves_2 = []
        self.generate_leaves(root2, leaves_2)
        return leaves_1 == leaves_2

        