
class Solution:
    #   递归
    def inorderTraversal(self, root):
        if not root:
            return []
        r1 = self.inorderTraversal(root.left)
        r2 = self.inorderTraversal(root.right)
        res = r1+[root.val]+r2
        return res

    def inorderTraversal(self, root):
        if not root:
            return []
        stack = []
        res = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            n = stack.pop()
            res.append(n.val)
            curr = n.right
        return res
