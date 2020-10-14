# 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        # 生成前缀和列表之后比较
        pre_sum = [0]
        for i, num in enumerate(nums):
            pre_sum.append(pre_sum[i] + num)

        cur = 1
        while cur < len(pre_sum):
            left = pre_sum[cur - 1]
            mid = pre_sum[cur]
            right = pre_sum[-1] - mid
            if left == right:
                return cur - 1
            cur += 1
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        s = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            # 如果存在中间索引，那么2*左侧=左+右，加上索引数，等于数组元素和
            if num + 2 * left == s:
                return i
            left += num
        return -1
