class Solution(object):
    def minDeletions(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        used = set()
        deletions = 0

        for count in freq.values():
            while count > 0 and count in used:
                count -= 1
                deletions += 1
            used.add(count)

        return deletions