import copy

result = []
nums = [1, 2, 3]


def main():
    choices = nums  # 选择列表
    track = []  # 路径
    backtrack(track, choices)
    return result


def backtrack(track, choices):
    # 当路径等于整数个数时，表示已经完成一次排列，结束
    if len(track) == len(nums):
        result.append(track)
        return

    for idx, choice in enumerate(choices):
        # 因为函数参数为可变参数，每个子递归必须深拷贝传递
        _track = copy.deepcopy(track)
        _choices = copy.deepcopy(choices)

        # 决策
        _track.append(choice)  # 把选择加入到路径中
        _choices.pop(idx)  # 把选择从选择列表中移除
        backtrack(_track, _choices)  # 交给下一个节点去做决策
        # 撤销决策
        # 对_track和_choices的改动不会影响到原路径和选择列表，可略去


if __name__ == '__main__':
    print(main())
