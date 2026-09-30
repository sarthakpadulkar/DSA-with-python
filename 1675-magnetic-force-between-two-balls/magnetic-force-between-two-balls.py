class Solution(object):
    def maxDistance(self, position, m):
        position.sort()

        def canPlace(distance):
            count = 1
            last = position[0]

            for pos in position[1:]:
                if pos - last >= distance:
                    count += 1
                    last = pos

                    if count >= m:
                        return True

            return False

        left = 1
        right = position[-1] - position[0]

        while left <= right:
            mid = left + (right - left) // 2

            if canPlace(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
