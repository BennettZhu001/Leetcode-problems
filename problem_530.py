# 530.py


# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.


from problem_104 import *


class Solution:
    def get_traversal_order(self, root):
        if not root:
            return []
        res = self.get_traversal_order(root.left)
        res.append(root.val)
        res += self.get_traversal_order(root.right)
        return res

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        order = self.get_traversal_order(root)
        min_abs = inf
        for i in range(len(order) - 1):
            min_abs = min(min_abs, order[i + 1] - order[i])
        return min_abs
