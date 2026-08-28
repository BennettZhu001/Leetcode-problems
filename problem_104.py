# Maximum depth of binary tree
#

from collections import deque

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth_BFS(root: Optional[TreeNode]) -> int:
    # DFS or BFS.
    # Let's do BFS. Terminate the problem when q is empty.
    if not root:
        return 0
    q = deque()
    q.append(root)
    current_depth = 0
    while q:
        for _ in range(len(q)):
            front = q.popleft()
            if front.left is not None:
                q.append(front.left)
            if front.right is not None:
                q.append(front.right)
        current_depth += 1
    return current_depth


def maxDepth_DFS(root: Optional[TreeNode]) -> int:
    # DFS
    if not root:
        return 0

    return 1 + max(maxDepth_DFS(root.left), maxDepth_DFS(root.right))
