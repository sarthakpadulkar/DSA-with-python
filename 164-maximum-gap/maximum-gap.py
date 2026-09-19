class Solution(object):
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        gap = (max_val - min_val + n - 2) // (n - 1)

        bucket_count = (max_val - min_val) // gap + 1

        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        used = [False] * bucket_count

        for num in nums:
            idx = (num - min_val) // gap
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
            used[idx] = True

        answer = 0
        previous_max = min_val

        for i in range(bucket_count):
            if not used[i]:
                continue

            answer = max(answer, bucket_min[i] - previous_max)
            previous_max = bucket_max[i]

        return answer
