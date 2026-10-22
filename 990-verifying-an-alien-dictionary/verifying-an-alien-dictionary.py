
class Solution:
    def isAlienSorted(self, words, order):
        rank = {}

        for i in range(len(order)):
            rank[order[i]] = i

        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            j = 0

            while j < len(a) and j < len(b):
                if a[j] != b[j]:
                    if rank[a[j]] > rank[b[j]]:
                        return False
                    break
                j += 1

            if j == len(b) and len(a) > len(b):
                return False

        return True
