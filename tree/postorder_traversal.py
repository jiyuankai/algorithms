
class Solution:
    #   递归
    def postorderTraversal(self, root):
        if not root:
            return []
        r1 = self.postorderTraversal(root.left)
        r2 = self.postorderTraversal(root.right)
        res = r1+r2+[root.val]
        return res

    def postorderTraversal(self, root):
        if not root:
            return []
        s1 = [root]
        s2 = []
        res = []
        while s1:
            n = s1.pop()
            s2.append(n)
            if n.right:
                s2.append(n.right)
            if n.left:
                s2.append(n.left)
        while s2:
            res.append(s2.pop().val)
        return res
