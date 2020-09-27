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

        def helper(node, next):
            if not node:
                return None
            node.next = next
            node.left = helper(node.left, node.right)
            node.right = helper(node.right, node.next.left if node.next else None)
            return node
        return helper(root, None)

'''
3）循环
对于非叶子节点，它的左孩子next指向右孩子，右孩子指向它的next对应节点的左孩子。
'''


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        node = root
        while node.left:
            head = node
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            node = node.left
        return root


# 117. Populating Next Right Pointers in Each Node II
"""
层序遍历，略

和116思路类似，但是因为此时树不是完美二叉树，所以下一层的起点不一定在最左孩子。
从根节点开始，通过遍历第n层，可以构建出n+1层的链表。每一层看作是一次链表遍历
三个变量
head：下一层链表的头结点
prev：前驱节点
cur： 当前层的游标，用来遍历当前层链表
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            # 从head头结点开始遍历
            cur = head
            # 此时head被赋予新的含义，即下一层的头结点
            # prev是遍历下一层的游标
            prev = head = None
            while cur:
                # 1）若prev尚未被赋值，说明遇到的是下一层的起始节点
                # head当前层的左/右孩子即为下一层的链表头，prev指向头，初始化
                # 2）若prev已经赋值，说明已经初始化，将他指向下一节点
                if cur.left:
                    if prev:
                        prev.next = cur.left
                        prev = prev.next
                    else:
                        prev = head = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                        prev = prev.next
                    else:
                        prev = head = cur.right
                cur = cur.next
        return root


