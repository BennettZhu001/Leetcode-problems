# 653.py

# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

from init import *


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root.left and not root.right:
            return False
        visited = set()
        q = deque()
        q.append(root)
        while q:
            front = q.popleft()
            if k - front.val in visited:
                return True
            visited.add(front.val)
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)

        return False
