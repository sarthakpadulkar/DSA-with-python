class Solution(object):
    def fullJustify(self, words, maxWidth):
       
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0

           
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - line_length

           
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                gaps = num_words - 1
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""
                for k in range(i, j - 1):
                    line += words[k]
                    spaces = spaces_per_gap
                    if k - i < extra_spaces:
                        spaces += 1
                    line += " " * spaces

                line += words[j - 1]

            result.append(line)
            i = j

        return result