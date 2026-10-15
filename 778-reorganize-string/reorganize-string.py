class Solution(object):
    def reorganizeString(self, s):
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        max_freq = max(freq)
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = [''] * len(s)
        max_char = freq.index(max_freq)

        i = 0
        while freq[max_char] > 0:
            res[i] = chr(max_char + ord('a'))
            i += 2
            freq[max_char] -= 1

        for j in range(26):
            while freq[j] > 0:
                if i >= len(s):
                    i = 1
                res[i] = chr(j + ord('a'))
                i += 2
                freq[j] -= 1

        return ''.join(res)