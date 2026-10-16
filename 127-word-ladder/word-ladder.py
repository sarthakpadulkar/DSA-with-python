class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = [(beginWord, 1)]
        visited = {beginWord}
        front = 0

        while front < len(queue):
            word, steps = queue[front]
            front += 1

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, steps + 1))

        return 0