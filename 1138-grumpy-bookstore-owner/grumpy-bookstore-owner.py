
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        total = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]

        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra

        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                extra += customers[i]

            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]

            max_extra = max(max_extra, extra)

        return total + max_extra
