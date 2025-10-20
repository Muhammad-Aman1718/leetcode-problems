# Binary Tree Postorder Traversal

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]


# Example 3:

# Input: root = []
# Output: []

# Example 4:

# Input: root = [1]
# Output: [1]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)


# postorder traversal
# Rule for postorder traversal: Left -> Right -> Root


class Solution:
    def __init__(self) -> None:
        self.result: list[int] = []

    def postOrder(self, root: "TreeNode |None "):
        if root == None:
            return

        self.postOrder(root.left)
        self.postOrder(root.right)
        self.result.append(root.val)

    def postorderTraversal(self, root: "TreeNode") -> list[int]:

        self.postOrder(root)
        return self.result


obj = Solution()
print(obj.postorderTraversal(root))
