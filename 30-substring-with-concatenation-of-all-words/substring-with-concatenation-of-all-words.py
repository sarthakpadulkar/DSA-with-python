class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        need = Counter(words)
        result = []

        # Try every possible alignment
        for offset in range(word_len):
            left = offset
            right = offset

            window = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                # Word is not required -> reset window
                if word not in need:
                    window.clear()
                    count = 0
                    left = right
                    continue

                window[word] = window.get(word, 0) + 1
                count += 1

                # Too many occurrences of this word
                while window[word] > need[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

                # Exactly all words are present
                if count == word_count:
                    result.append(left)

                    # Move left forward to look for next window
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

        return result


