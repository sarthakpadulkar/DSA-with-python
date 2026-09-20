class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        
        if k == n:
            return sum(cardPoints)
        
        window_size = n - k
        window_sum = sum(cardPoints[:window_size])
        min_sum = window_sum
        
        for i in range(window_size, n):
            window_sum += cardPoints[i]
            window_sum -= cardPoints[i - window_size]
            min_sum = min(min_sum, window_sum)
        
        return sum(cardPoints) - min_sum
