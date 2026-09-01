# 450 problem


# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# 1) Search for a node to remove.
# 2) If the node is found, delete the node.

from problem_104 import *


class Solution:
    # iterative Solution

    def find_maximum_left_subtree(self, root):
        # This is a function finding the maximum node in the left subtree of the root
        # and return a tuple of the node and the parent of the node.
        # root is not None by default

        if not root.left:
            # return None, root means that there are not any nodes in left subtree.
            return None, root

        curr_node = root.left
        curr_parent = root

        while curr_node.right:
            curr_parent = curr_node
            curr_node = curr_node.right

        return curr_node, curr_parent

    def find_minimum_right_subtree(self, root):
        # This is a function finding the minimum node in the right subtree of the root
        # and return a tuple of the node and the parent of the node.
        # root is not None by default

        if not root.right:
            # return None, root means that there are not any nodes in right subtree.
            return None, root

        curr_node = root.right
        curr_parent = root

        while curr_node.left:
            curr_parent = curr_node
            curr_node = curr_node.left
        return curr_node, curr_parent

    def deleteRoot(self, root):

        # This is a function deleting the root of a tree. We will use the two functions defined above to
        # implement this deleteRoot function.
        # By default, root is not None

        if (not root.left) and (not root.right):
            return None
        elif root.left:
            node, parent_node = self.find_maximum_left_subtree(root)
            if node == root.left and parent_node == root:
                tempt = TreeNode(node.val, node.left, root.right)
                return tempt
            else:
                parent_node.right = node.left
                tempt = TreeNode(node.val, root.left, root.right)
                return tempt

        else:
            node, parent_node = self.find_minimum_right_subtree(root)
            if node == root.right and parent_node == root:
                tempt = TreeNode(node.val, node.right, root.left)
                return tempt
            else:
                parent_node.left = node.right
                tempt = TreeNode(node.val, root.left, root.right)
                return tempt

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        dummy_node = TreeNode(float("inf"), root, None)
        curr_parent = dummy_node
        curr_node = root

        # curr_position is a variable for the current_node.
        # "left" means that curr_node is a left child of the curr_parent.

        curr_position = "left"

        while curr_node:
            if curr_node.val == key:
                if curr_position == "left":
                    curr_parent.left = self.deleteRoot(curr_node)
                else:
                    curr_parent.right = self.deleteRoot(curr_node)
                return dummy_node.left
            elif curr_node.val < key:
                curr_parent = curr_node
                curr_node = curr_node.right
                curr_position = "right"
            else:
                curr_parent = curr_node
                curr_node = curr_node.left
                curr_position = "left"

        return dummy_node.left

    def deleteNode_recursive(self, root, key):
        if not root:
            return root

        if root.val == key:
            return self.deleteRoot(root)
        elif root.val < key:
            root.right = self.deleteNode_recursive(root.right, key)
            return root
        else:
            root.left = self.deleteNode_recursive(root.left, key)
            return root


def insert(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def inorder(root):
    if not root:
        return []

    return inorder(root.left) + [root.val] + inorder(root.right)


def run_tests():
    test_cases = [
        ([], 5, []),  # empty tree
        ([5], 5, []),  # delete only node
        ([5, 3, 7], 3, [5, 7]),  # leaf
        ([5, 3, 7, 2], 3, [2, 5, 7]),  # one child
        ([5, 3, 7, 2, 4, 6, 8], 3, [2, 4, 5, 6, 7, 8]),
        ([5, 3, 7, 2, 4, 6, 8], 5, [2, 3, 4, 6, 7, 8]),
        ([5, 3, 7, 2, 4, 6, 8], 99, [2, 3, 4, 5, 6, 7, 8]),
    ]

    solution = Solution()

    for values, key, expected in test_cases:
        root = None
        for value in values:
            root = insert(root, value)

        result = solution.deleteNode_recursive(root, key)
        actual = inorder(result)

        assert actual == expected, (
            f"Failed for key={key}: expected {expected}, got {actual}"
        )

    print("All tests passed!")


def main():
    run_tests()


if __name__ == "__main__":
    main()
