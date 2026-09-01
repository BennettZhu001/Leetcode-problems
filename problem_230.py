# problem 230

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


from problem_104 import *


class Solution:
    def BST_2_sortedArray(self, root):
        if not root:
            return []
        return (
            self.BST_2_sortedArray(root.left)
            + [root.val]
            + self.BST_2_sortedArray(root.right)
        )

    def BST_2_sortedArray_Stack(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        curr = root.left
        while curr:
            stack.append(curr)
            curr = curr.left
        while stack:
            top = stack.pop()
            res.append(top.val)
            if top.right:
                curr = top.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArray = self.BST_2_sortedArray(root)
        return sortedArray[k - 1]

    def kthSmallest_stack(self, root, k):
        count = 0
        stack = [root]
        curr = root.left
        while curr:
            stack.append(curr)
            curr = curr.left
        while stack:
            top = stack.pop()
            count += 1
            if count == k:
                return top.val
            if top.right:
                curr = top.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
