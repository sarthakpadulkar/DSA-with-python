class Solution:
    def numSubarraysWithSum(self, nums, goal):
        def atMost(k):
            if k < 0:
                return 0

            left = 0
            total = 0
            count = 0

            for right in range(len(nums)):
                total += nums[right]

                while total > k:
                    total -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return atMost(goal) - atMost(goal - 1)