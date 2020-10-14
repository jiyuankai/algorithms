# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda i: i[0])
        res = [intervals[0]]
        for curr in intervals[1:]:
            prev = res[-1]
            # 若当前区间的开始时间在前一个区间内，需要合并
            if curr[0] <= prev[1]:
                # 后开始的可能早结束
                prev[1] = max(curr[1], prev[1])
            # 反之，不相交直接加入结果
            else:
                res.append(curr)
        return res
