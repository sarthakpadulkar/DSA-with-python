class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)

        if m * k > n:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        def canMake(day):
            bouquets = 0
            consecutive = 0

            for bloom in bloomDay:
                if bloom <= day:
                    consecutive += 1

                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0

                        if bouquets >= m:
                            return True
                else:
                    consecutive = 0

            return False

        while left < right:
            mid = left + (right - left) // 2

            if canMake(mid):
                right = mid
            else:
                left = mid + 1

        return left
