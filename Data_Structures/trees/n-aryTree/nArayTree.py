# n-ary tree


class TreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.children: list["TreeNode"] = []

    def addChild(self, childNode: "TreeNode") -> None:
        self.children.append(childNode)


root = TreeNode(1)
root.addChild(TreeNode(2))
root.addChild(TreeNode(3))
root.addChild(TreeNode(4))
root.addChild(TreeNode(5))
root.children[0].addChild(TreeNode(6))
root.children[0].addChild(TreeNode(7))


class Solution:
    def postorder_traversal(self, root: "TreeNode") -> list[int]:
        # """Recursive postorder traversal: children -> root"""
        if not root:
            return []

        result: list[int] = []
        for child in root.children:
            result.extend(self.postorder_traversal(child))
        result.append(root.data)

        return result

    def postorder(self, root: "TreeNode") -> list[int]:
        # """Wrapper function (optional)"""
        return self.postorder_traversal(root)


tree = Solution()
print(tree.postorder_traversal(root))
