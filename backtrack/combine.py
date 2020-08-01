import copy
from pprint import pprint

result = []


def combine(n, k):
    track = []
    bt(track, 1, n, k)
    return result


def bt(track, start, n, k):
    if len(track) == k:
        result.append(track)
        return
    for c in range(start, n + 1):
        track.append(c)
        bt(copy.deepcopy(track), start+1, n, k)
        track.pop()


if __name__ == '__main__':
    n, k = 4, 2
    pprint(combine(n, k))
