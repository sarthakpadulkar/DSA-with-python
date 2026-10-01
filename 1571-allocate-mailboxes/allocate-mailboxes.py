class Solution(object):
    def minDistance(self, houses, k):
        houses.sort()
        n = len(houses)

        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                mid = (i + j) // 2
                for p in range(i, j + 1):
                    cost[i][j] += abs(houses[p] - houses[mid])

        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for m in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(m - 1, i):
                    dp[m][i] = min(
                        dp[m][i],
                        dp[m - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
