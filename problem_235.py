# problem 235

# 235. Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# previously, we solved the lowest common ancestor of the binary tree. We used Breadth first search for binary tree
# and record the parents of each node. And then find the lowest common ancestor.
# For BST, it is easier to find the lowest common ancestor since it is ordered.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        curr = root
        while True:
            if min_val < curr.val and max_val > curr.val:
                break
            elif min_val == curr.val or max_val == curr.val:
                break
            elif max_val < curr.val:
                curr = curr.left
            elif min_val > curr.val:
                curr = curr.right
        return curr
