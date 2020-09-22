# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #   递归
    def preorderTraversal(self, root):
        if not root:
            return []
        r1 = self.preorderTraversal(root.left)
        r2 = self.preorderTraversal(root.right)
        res = [root.val]+r1+r2
        return res

    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            n = stack.pop()
            res.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)

        return res
