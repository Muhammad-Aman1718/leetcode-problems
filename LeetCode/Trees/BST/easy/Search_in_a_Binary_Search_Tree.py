# Search in a Binary Search Tree

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# Example 1:

# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

# Example 2:

# Input: root = [4,2,7,1,3], val = 5
# Output: []


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


class Solution:
    def searchBST(self, root: "TreeNode | None", val: int) -> "TreeNode | None":
        if root == None:
            return None
        curr = root
        while curr != None:
            if curr.val == val:
                return curr
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right

        return None


obj = Solution()
print(obj.searchBST(root, 1))
