import random
import string


def main():
    ids = [
        # '111111', '222222', '333333',
           '444444', '555555',
           # '666666', '777777', '8888888',
           # '9999999', '0000000',
           # 'aaaaaaa', 'bbbbb', 'cccccc',
           # 'dddddd', 'eeeeee',
   ]
    # ids = ['a' * random.randint(5, 15) for _ in range(random.randint(100, 200))]
    pairs = divide_commodity_ids(ids)
    print(pairs, len(ids), len(pairs))


def divide_commodity_ids(comm_ids, max_cnt=3):
    pairs = []
    start = 0
    while start < len(comm_ids) - 1:
        pairs.append(comm_ids[start: start + max_cnt])
        start += max_cnt
    return pairs



# def divide_commodity_ids(comm_ids, max_len=30):
#     id_lens = list(map(len, comm_ids))
#     pre_sum = get_pre_sum(id_lens)
#     pos = [0]
#     for p1, n in enumerate(pre_sum):
#         top = pos[-1]
#         delta = n - pre_sum[top] + (p1 - top)
#         if delta > max_len:
#             pos.append(p1 - 1)
#         elif delta == max_len:
#             pos.append(p1)
#     end = len(pre_sum) - 1
#     if end not in pos:
#         pos.append(end)
#     pairs = []
#     start = 0
#     for i in filter(None, pos):
#         pairs.append(comm_ids[start:i])
#         start = i
#
#     res = []
#     for pair in pairs:
#         s = ','.join(pair)
#         if len(s) > max_len:
#             print(len(s), pair, max_len)
#         assert len(s) <= max_len
#         res.extend(pair)
#
#     assert set(res) == set(comm_ids)
#     return pairs



def get_pre_sum(nums):
    pre_sum = [0 for i in range(len(nums) + 1)]
    for idx, length in enumerate(nums):
        pre_sum[idx + 1] = pre_sum[idx] + nums[idx]
    return pre_sum


if __name__ == '__main__':
    main()
