# 116. Populating Next Right Pointers in Each Node

'''
1） BFS
从右至左层序遍历树
后继节点next指针指向前一节点
时间复杂度 On (每个节点都被遍历到了)
空间复杂度 On (队列最大长度为n/2即完全二叉树叶节点个数)
'''


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = [root]
        while q:
            size = len(q)
            next = None
            while size:
                node = q.pop(0)
                node.next = next
                next = node
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                size -= 1
        return root


'''
2）递归
节点的左孩子总是指向右孩子，有孩子指向节点next对应的节点的左孩子(如果有，否则None)
后继节点next指针指向前一节点
时间复杂度 On (每个节点都被遍历了)
空间复杂度 On (递归栈，每个节点都入栈了)
'''


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def helper(node, next):
            if not node:
                return None
            node.next = next
            node.left = helper(node.left, node.right)
            node.right = helper(node.right, node.next.left if node.next else None)
            return node
        return helper(root, None)
