# 394. Decode String


class Solution:
    def decodeString(self, s: str) -> str:

        def helper(i):
            multi = 0
            res = ""
            while i < len(s):
                c = s[i]
                if c == '[':
                    # 遇到左括号，开始递归，将括号内子串递归调用
                    # 返回刷新外部i值，以及括号子串结果
                    i, next_res = helper(i + 1)
                    res += multi * next_res
                    # 乘数清零
                    multi = 0
                elif c == ']':
                    # 右括号是递归结束条件
                    return i, res
                elif ord('0') <= ord(c) <= ord('9'):
                    multi = multi * 10 + int(c)
                else:
                    res += c
                i += 1
            return res
        return helper(0)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multi = 0
        res = ""
        for c in s:
            if c == '[':
                stack.append([res, multi])
                res, multi = "", 0
            elif c == ']':
                # 如果嵌套括号，这里的prev_res也是以[为边界的局部res
                prev_res, prev_multi = stack.pop()
                res = prev_res + prev_multi * res
            elif ord('0') <= ord(c) <= ord('9'):
                multi = multi * 10 + int(c)
            else:
                # 字符串可以看做以左括号分隔的两部分
                # res从左括号[开始累加，到右括号]结束，等于括号中的字符串
                res += c
        return res
