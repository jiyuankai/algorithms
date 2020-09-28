# 236. Lowest Common Ancestor of a Binary Tree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = None
        # dfs返回以root为根节点的树，是否存在p和q节点
        def dfs(root, p, q):
            if not root:
                return False
            lson = dfs(root.left, p, q)
            rson = dfs(root.right, p, q)
            # 成为公共祖先条件：左右子树都存在p和q节点 或者 自己本身是pq之一，左右子树满足存在另一个节点即可
            if lson and rson or ((lson or rson) and (root.val == p.val or root.val == q.val)):
                self.ancestor = root
            # 发现自己是pq，或者左右子树有pq，就返回True
            return (root.val == p.val or root.val == q.val) or lson or rson
        dfs(root, p, q)
        return self.ancestor
