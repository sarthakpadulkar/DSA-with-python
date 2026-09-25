import random

class Solution(object):

    def __init__(self, w):
        self.prefix = []
        total = 0

        for weight in w:
            total += weight
            self.prefix.append(total)

        self.total = total

    def pickIndex(self):
        target = random.randint(1, self.total)

        left = 0
        right = len(self.prefix) - 1

        while left < right:
            mid = (left + right) // 2

            if self.prefix[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left
