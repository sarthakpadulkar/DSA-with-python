class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = ["", "", "abc", "def", "ghi", "jkl",
                 "mno", "pqrs", "tuv", "wxyz"]

        res = [""]

        for d in digits:
            temp = []
            for combo in res:
                for c in phone[int(d)]:
                    temp.append(combo + c)
            res = temp

        return res