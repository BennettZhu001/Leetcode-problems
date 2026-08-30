# 701.py

# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


from problem_104 import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val, None, None)
            return root
        pointer = root
        while pointer:
            if pointer.val < val and pointer.right:
                pointer = pointer.right
            elif pointer.val < val and not pointer.right:
                pointer.right = TreeNode(val, None, None)
                return root
            elif pointer.val > val and pointer.left:
                pointer = pointer.left
            elif pointer.val > val and not pointer.left:
                pointer.left = TreeNode(val, None, None)
                return root
        return root

    # This solution turns out to be slow.
    # You should break the if, elif, elif, elif into nested if else in order to reduce the number of
    # conditions you need to check.
    # Essentially, if you nest the conditions, you are doing binary search.
    # If you don't do nessted conditions, you are searching the while space linearly.
    #
    #
    #

    def insertIntoBST_faster(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        new_node = TreeNode(val, None, None)
        if not root:
            root = new_node
            return root
        pointer = root
        while pointer:
            if pointer.val < val:
                if pointer.right:
                    pointer = pointer.right
                else:
                    pointer.right = new_node
                    break
            else:
                if pointer.left:
                    pointer = pointer.left
                else:
                    pointer.left = new_node
                    break

        return root
