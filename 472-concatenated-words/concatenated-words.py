class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        memo = {}

        def can_form(word, start, count):
            if start == len(word):
                return count >= 2

            key = (word, start, count)
            if key in memo:
                return memo[key]

            for end in range(start + 1, len(word) + 1):
                prefix = word[start:end]

                if prefix in word_set:
                    if can_form(word, end, count + 1):
                        memo[key] = True
                        return True

            memo[key] = False
            return False

        result = []

        for word in words:
            word_set.remove(word)

            if can_form(word, 0, 0):
                result.append(word)

            word_set.add(word)

        return result