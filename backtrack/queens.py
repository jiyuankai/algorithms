import copy
from pprint import pprint

n = 8
result = []


def main():
    # 构造N*N的棋盘，用二维数组表示
    board = []
    for _ in range(n):
        row = ['_' for _ in range(n)]
        board.append(row)
    backtrack(board, 0)
    return result


# def 回溯算法函数（路径，选择列表）
# 0~row上Queen的排布即为「路径」, 而board[row]即为「选择列表」
def backtrack(board, row):

    # 定义递归基，结束条件: 当row超过了棋盘行数
    if row == len(board):
        result.append(board)
        return

    # 第row行上，所有的列，都可以作为放置Queen的选择
    choices = len(board[row])
    for col in range(choices):
        # 过滤掉不符合规则的选择
        if not is_valid(board, row, col):
            continue

        # 做选择
        # 将当前格子放上Queen
        board[row][col] = 'Q'
        backtrack(copy.deepcopy(board), row+1)
        # 撤销选择
        board[row][col] = '_'
        # PS: 不需要编辑选择列表，循环入口会用路径对选择列表做过滤


def is_valid(board, row, col):
    # 检查列上是不是已经放置了Queen
    # col=col, row=[0, row)
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # 检查右上方向是不是已经放置了Queen
    i, j = row - 1, col + 1  # 从右上格开始
    while i >= 0 and j < n:  # 直到棋盘边界(row < 0 或者 col >= n)
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    # 检查左上方向是不是已经放置了Queen
    i, j = row - 1, col - 1  # 从左上格开始
    while i >= 0 and j >= 0:  # 直到棋盘边界(row < 0 或者 col < 0)
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    return True


if __name__ == '__main__':
    pprint(main())
    print(len(result))

