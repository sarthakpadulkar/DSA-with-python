class Solution(object):
    def isNumber(self, s):
        
        s = s.strip()

        num_seen = False
        dot_seen = False
        exp_seen = False
        num_after_exp = True

        for i, ch in enumerate(s):
            if ch.isdigit():
                num_seen = True
                if exp_seen:
                    num_after_exp = True

            elif ch in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            elif ch == '.':
                if dot_seen or exp_seen:
                    return False
                dot_seen = True

            elif ch in 'eE':
                if exp_seen or not num_seen:
                    return False
                exp_seen = True
                num_after_exp = False

            else:
                return False

        return num_seen and num_after_exp