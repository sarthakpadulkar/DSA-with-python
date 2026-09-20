class Solution(object):
    def checkSubarraySum(self, nums, k):
        seen = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i

        return False
