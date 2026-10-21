
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()

        first = len(s) % k
        result = s[:first]

        for i in range(first, len(s), k):
            if result:
                result += "-"
            result += s[i:i + k]

        return result
