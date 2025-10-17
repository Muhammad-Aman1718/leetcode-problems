# Binary Tree Definition
# A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.

# Properties of Binary Trees:
# 1. Each node contains a value.
# 2. Each node has at most two children.
# 3. The left child's value is less than its parent's value.
# 4. The right child's value is greater than its parent's value.
# 5. There is no cycle in a binary tree.
# 6. Directed Trees: The edges in a binary tree are directed from parent to child nodes.
# 7. Number of edges is one less than the number of nodes (n nodes have n-1 edges).

# Terminologies:
# 1. Node: The basic unit of a binary tree, containing data and references to its children.
# 2. Root: The topmost node of the tree.
# 3. Leaf: A node that does not have any children.
# 4. Edge: The connection between a parent node and a child node.
# 5. Leaf Node: A node that does not have any children.
# 6. Depth: The length of the path from the root to a specific node.
# 7. Height: The length of the longest path from a node to a leaf node.

# Types of Binary Trees:
# 1. Full Binary Tree: Every node has either 0 or 2 children.
# 2. Complete Binary Tree: All levels are fully filled except possibly the last level, which is filled from left to right.
# 3. Perfect Binary Tree: All internal nodes have two children, and all leaf nodes are at the same level.
# 4. Balanced Binary Tree: The height of the two subtrees of any node never differs by more than one.
# 5. Degenerate (or Pathological) Tree: Each parent node has only one child, resembling a linked list.
# 6. Skewed Tree: All nodes have only one child, either all left or all right.



class TreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
print(root.left.data)


# Full Binary Tree Example
full_root = TreeNode(1)
full_root.left = TreeNode(2)
full_root.right = TreeNode(3)
full_root.left.left = TreeNode(4)
full_root.left.right = TreeNode(5)
full_root.right.left = TreeNode(6)
full_root.right.right = TreeNode(7)

# Complete Binary Tree Example
complete_root = TreeNode(1)
complete_root.left = TreeNode(2)
complete_root.right = TreeNode(3)
complete_root.left.left = TreeNode(4)
complete_root.left.right = TreeNode(5)
complete_root.right.left = TreeNode(6)

# Perfect Binary Tree Example
perfect_root = TreeNode(1)
perfect_root.left = TreeNode(2)
perfect_root.right = TreeNode(3)
perfect_root.left.left = TreeNode(4)
perfect_root.left.right = TreeNode(5)
perfect_root.right.left = TreeNode(6)
perfect_root.right.right = TreeNode(7)

# Balanced Binary Tree Example
balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(3)
balanced_root.left.left = TreeNode(4)
balanced_root.left.right = TreeNode(5)

# Degenerate Tree Example
degenerate_root = TreeNode(1)
degenerate_root.right = TreeNode(2)
degenerate_root.right.right = TreeNode(3)
degenerate_root.right.right.right = TreeNode(4)

# Skewed Tree Example (Right Skewed)
skewed_root = TreeNode(1)
skewed_root.right = TreeNode(2)
skewed_root.right.right = TreeNode(3)
skewed_root.right.right.right = TreeNode(4)