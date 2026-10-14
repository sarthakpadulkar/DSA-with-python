class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))

        if len(diff) != 2:
            return False

        return diff[0] == diff[1][::-1]