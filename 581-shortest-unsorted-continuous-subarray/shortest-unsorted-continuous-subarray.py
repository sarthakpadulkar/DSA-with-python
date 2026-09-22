class Solution(object):
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)

        left = 0
        right = len(nums) - 1

        while left < len(nums) and nums[left] == sorted_nums[left]:
            left += 1

        while right >= 0 and nums[right] == sorted_nums[right]:
            right -= 1

        if left >= right:
            return 0

        return right - left + 1

