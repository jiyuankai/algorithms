from collections import defaultdict
s = 'ADOBECODEBANC'
t = 'ABC'


def main():
    left = right = match = 0
    sub_str = ""
    window = defaultdict(int)
    needs = {}
    min_len = len(s)
    # 初始化needs
    for i in t:
        cnt = needs.get(i, 0)
        needs[i] = cnt + 1

    # 右指针到达字符串尾部结束
    while right < len(s):
        c1 = s[right]
        if c1 in needs:
            # 若字符c1符合子串，加入window
            window[c1] += 1
            # c1字符的数量符合子串，match计数+1
            if window[c1] == needs[c1]:
                match += 1
        right += 1

        # 当match计数器和needs字符数相等，说明当前window中的已经串包含目标子串中所需的字符
        while match == len(needs):
            # 此时，记录当前match的子串
            if min_len > right - left:
                min_len = right - left
                sub_str = s[left:right]
            # 右指针停止，左指针右移缩小窗口，寻找最小子串
            c2 = s[left]
            if c2 in needs:
                window[c2] -= 1
                if window[c2] < needs[c2]:
                    match -= 1
            left += 1
    return sub_str


if __name__ == '__main__':
    print(main())
