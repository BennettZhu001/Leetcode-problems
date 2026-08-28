# 111. py


# BFS solving the problem. BFS essentially visit the nodes level by level
# At each level, if any node dequeues and it has no children, i.e. it is a leaf node, the program terminates
# The program terminates when the first case happen


from collections import deque

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        if root is None:
            return 0
        q = deque()
        q.append(root)
        current_depth = 1
        while q:
            length = len(q)
            for _ in range(length):
                front = q.popleft()
                if front.left is None and front.right is None:
                    return current_depth

                if front.left is not None:
                    q.append(front.left)
                if front.right is not None:
                    q.append(front.right)
            current_depth += 1
