class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2

        a = nums[:mid][::-1]
        b = nums[mid:][::-1]

        nums[::2] = a
        nums[1::2] = b
