class Solution(object):
    def getMaxLen(self, nums):
       
        pos = 0
        neg = 0
        ans = 0

        for num in nums:
            if num > 0:
                pos = pos + 1
                neg = neg + 1 if neg > 0 else 0

            elif num < 0:
                old_pos = pos
                old_neg = neg

                pos = old_neg + 1 if old_neg > 0 else 0
                neg = old_pos + 1

            else:
                pos = 0
                neg = 0

            ans = max(ans, pos)

        return ans
