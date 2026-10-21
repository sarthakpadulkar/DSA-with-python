
class Solution(object):
    def customSortString(self, order, s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        result = ""

        for ch in order:
            if ch in count:
                result += ch * count[ch]
                count[ch] = 0

        for ch in s:
            if count.get(ch, 0) > 0:
                result += ch
                count[ch] -= 1

        return result
