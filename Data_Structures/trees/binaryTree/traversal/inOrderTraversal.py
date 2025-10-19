# Traversal Examples (Inorder, Preorder, Postorder, Level-order) can be implemented as needed.
# Additional operations like insertion, deletion, searching, and balancing can also be implemented as needed.


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


# inorder traversal
# Rule for inorder traversal: Left -> Root -> Right
class Solution:
    def __init__(self) -> None:
        self.result: list[int] = []

    def inOrder(self, root: "TreeNode |None "):
        if root == None:
            return

        self.inOrder(root.left)
        self.result.append(root.val)
        self.inOrder(root.right)

    def inorderTraversal(self, root: "TreeNode") -> list[int]:

        self.inOrder(root)
        return self.result


obj = Solution()
print(obj.inorderTraversal(root))
