class Solution(object):
    def findShortestSubArray(self, nums):
        first = {}
        last = {}
        count = {}
        
        degree = 0
        
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            
            last[num] = i
            count[num] = count.get(num, 0) + 1
            degree = max(degree, count[num])
        
        answer = len(nums)
        
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                answer = min(answer, length)
        
        return answer
