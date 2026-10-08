class Solution(object):
    def myAtoi(self, s):
        index = 0
        length = len(s)
        while index < length and s[index] == ' ':
            index += 1
        sign = 1
        if index < length and s[index] == '-':
            sign = -1
            index += 1
        elif index < length and s[index] == '+':
            index += 1
        number = 0
        while index < length and '0' <= s[index] <= '9':
            digit = ord(s[index]) - ord('0')
            number = number * 10 + digit
            index += 1
        number *= sign
        minimum = -2**31
        maximum = 2**31 - 1
        if number < minimum:
            return minimum
        if number > maximum:
            return maximum
        return number