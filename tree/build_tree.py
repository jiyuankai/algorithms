'''
后续遍历结果，最后一个是根节点；前序遍历结果，第一个是根节点。
中序遍历结果中，根节点左边是左子树，右边是右子树。
递归
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 106. Construct Binary Tree from Inorder and Postorder Traversal
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
class Solution:

    def buildTree(self, inorder, postorder):
        val_idx_map = {}
        for i, v in enumerate(inorder):
            val_idx_map[v] = i

        def helper(start, end):
            if start > end:
                return None
            root = TreeNode(postorder.pop())
            root_idx = val_idx_map[root.val]
            root.right = helper(root_idx + 1, end)
            root.left = helper(start, root_idx - 1)
            return root
        return helper(0, len(postorder) - 1)

# 105. Construct Binary Tree from Preorder and Inorder Traversal
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]


class Solution:

    def buildTree(self, preorder, inorder):
        val_idx_map = {}
        for i, v in enumerate(inorder):
            val_idx_map[v] = i

        def helper(start, end):
            if start > end:
                return None
            root = TreeNode(preorder.pop(0))
            root_idx = val_idx_map[root.val]
            root.left = helper(start, root_idx - 1)
            root.right = helper(root_idx + 1, end)
            return root

        return helper(0, len(preorder) - 1)