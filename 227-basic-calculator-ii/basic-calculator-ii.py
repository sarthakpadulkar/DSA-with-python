class Solution:
    def calculate(self, s):
        stack = []
        number = 0
        operator = '+'

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                number = number * 10 + int(ch)

            if ch in '+-*/' or i == len(s) - 1:
                if operator == '+':
                    stack.append(number)
                elif operator == '-':
                    stack.append(-number)
                elif operator == '*':
                    stack.append(stack.pop() * number)
                elif operator == '/':
                    last = stack.pop()
                    result = abs(last) // number
                    if last < 0:
                        result = -result
                    stack.append(result)

                operator = ch
                number = 0

        return sum(stack)