import copy

result = []


def subsets(nums):
    track = []
    backtrack(track, 0, nums)
    return result


def backtrack(track, start, choices):
    # 与全排列不同，子序列的解为递归过程中所有的路径集合（不论是否满足结束条件）
    result.append(track)
    # 结束条件choices为空，递归基
    if start == len(choices):
        return
    for i, choice in enumerate(choices[start:]):
        # 做选择
        track.append(choice)
        # 选择过的元素在后续路径中不再出现，全局维度
        # i是基于start的索引，所以传递时要加上start
        backtrack(copy.deepcopy(track), start+i+1, choices)
        # 撤销选择
        track.pop()


if __name__ == '__main__':
    print(subsets([1, 2]))
