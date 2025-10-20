# Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:

# Input: root = [1,null,2]
# Output: 2

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


class Solution:
    def maxDepth(self, root: "TreeNode | None") -> int:
        # Base Case
        if root == None:
            return 0

        # Recursive Case
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        return max(leftHeight, rightHeight) + 1


obj = Solution()
print(obj.maxDepth(root))
