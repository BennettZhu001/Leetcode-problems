# 236


# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

from problem_104 import *


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # BFS to get parents dictionary
        if not root:
            return root
        if not root.left and not root.right:
            return root
        parents = {root: None}
        queue = deque()
        queue.append(root)
        while queue:
            front = queue.popleft()
            if front.left:
                queue.append(front.left)
                parents[front.left] = front
            if front.right:
                queue.append(front.right)
                parents[front.right] = front
            if p in parents and q in parents:
                break

        parents_p = []
        p_pointer = p
        parents_q = []
        q_pointer = q
        while p_pointer:
            parents_p.append(p_pointer)
            p_pointer = parents[p_pointer]
        while q_pointer:
            parents_q.append(q_pointer)
            q_pointer = parents[q_pointer]

        i = 1
        while i <= min(len(parents_p), len(parents_q)):
            if parents_p[-i] == parents_q[-i]:
                i += 1
            else:
                break
        return parents_p[-(i - 1)]
