# 112


# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.


from problem_104 import *
from collections import deque


class Solution:
    def hasPathSum_1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # BFS
        if not root:
            return False
        parents = {root: None}
        q = deque()
        q.append(root)
        while q:
            front = q.popleft()
            if front.left:
                q.append(front.left)
                parents[front.left] = front
            if front.right:
                q.append(front.right)
                parents[front.right] = front
            if not front.left and not front.right:
                ancester = parents[front]
                curr_sum = front.val
                while ancester:
                    curr_sum += ancester.val
                    ancester = parents[ancester]
                if curr_sum == targetSum:
                    return True
        return False

    def hasPathSum_2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # BFS
        if not root:
            return False
        q = deque()
        curr_sum = {}
        parents = {}
        q.append(root)
        curr_sum[root] = root.val
        parents[root] = None

        while q:
            front = q.popleft()
            if front.left:
                q.append(front.left)
                curr_sum[front.left] = curr_sum[front] + front.left.val
            if front.right:
                q.append(front.right)
                curr_sum[front.right] = curr_sum[front] + front.right.val
            if not front.left and not front.right and curr_sum[front] == targetSum:
                return True

        return False
