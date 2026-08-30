# 108.py


# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.


from init import *


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(nums[0])
        elif length == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])

        else:
            root = TreeNode(nums[length // 2])
            root.left = self.sortedArrayToBST(nums[: length // 2])
            root.right = self.sortedArrayToBST(nums[length // 2 + 1 :])

        return root


# The problem becomes much easier if you can deal with the edge cases properly
# Then you can solve the sortedArrayToBST in a very simple fashion.
