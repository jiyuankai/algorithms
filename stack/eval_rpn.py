s = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]


def main(nums):
    stack = []
    for num in nums:
        try:
            stack.append(int(num))
        except ValueError:
            b = stack.pop()
            a = stack.pop()
            if num == '+':
                c = a + b
            elif num == '-':
                c = a - b
            elif num == '*':
                c = a * b
            else:
                c = int(a / b)
            stack.append(c)
    return stack.pop()


if __name__ == '__main__':
    r = main(s)
    print(r)


class Solution:

    def isSymmetric(self, root):
        if not root:
            return True

        s1 = []
        r1 = []
        curr = root
        while curr or s1:
            while curr:
                s1.append(curr)
                curr = curr.left
            n = s1.pop()
            r1.append(n.val)
            curr = n.right

        s2 = []
        r2 = []
        curr = root
        while curr or s2:
            while curr:
                s2.append(curr)
                curr = curr.right
            n = s2.pop()
            r2.append(n.val)
            curr = n.left

        return r1[::-1] == r2

    def preorder(self, root):
        s = []
        res = []
        curr = root
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            n = s.pop()
            res.append(n.val)
            curr = n.right




