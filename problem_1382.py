# 1382.py medium level question


# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.


# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.


from problem_104 import *

# Definition for a binary tree node.


class Solution:
    def BSTtoSortedArray(self, root: Optional[TreeNode]):
        if not root:
            return []
        res = []
        res = self.BSTtoSortedArray(root.left)
        res.append(root.val)
        res += self.BSTtoSortedArray(root.right)
        return res

    def SortedArrayToBalancedBST(self, nums):
        length = len(nums)
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(nums[0])
        elif length == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        else:
            mid = length // 2
            root = TreeNode(nums[mid])
            root.left = self.SortedArrayToBalancedBST(nums[:mid])
            root.right = self.SortedArrayToBalancedBST(nums[mid + 1 :])

            return root

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.SortedArrayToBalancedBST(self.BSTtoSortedArray(root))


# Remark on this problem.
# In order to get this problem done or generally other medium level questions done, it usually
# takes two tricks that are used to solve two easy problems.
# For example, this problem can be solve by converting the BST to a sorted array and then converting the sorted array
# to a balanced BST. This medium problem is essentially two easy problems combined


# So this might be a great way of approaching the problem. First try to solve it in a stupid, brutal force way. Then improve and optimize it.
