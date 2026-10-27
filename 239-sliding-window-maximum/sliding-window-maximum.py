class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = []
        ans = []
        head = 0

        for i in range(len(nums)):
            if head < len(dq) and dq[head] <= i - k:
                head += 1

            while len(dq) > head and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                ans.append(nums[dq[head]])

        return ans