class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = {}
        queue = [beginWord]
        visited = {beginWord}
        found = False

        while queue and not found:
            nextQueue = []
            levelVisited = set()

            for word in queue:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue

                        newWord = word[:i] + ch + word[i + 1:]

                        if newWord not in wordSet or newWord in visited:
                            continue

                        if newWord not in parents:
                            parents[newWord] = []
                        parents[newWord].append(word)

                        if newWord not in levelVisited:
                            levelVisited.add(newWord)
                            nextQueue.append(newWord)

                        if newWord == endWord:
                            found = True

            visited.update(levelVisited)
            queue = nextQueue

        if not found:
            return []

        result = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)
        return result