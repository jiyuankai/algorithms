# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
                ans = mid
        return ans
