class Solution(object):
    def minWindow(self, s, t):
        
        from collections import Counter

        need = Counter(t)
        window = {}

        left = 0
        have = 0
        required = len(need)

        best_len = float('inf')
        best_left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

           
            if c in need and window[c] == need[c]:
                have += 1

            
            while have == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_char = s[left]
                window[left_char] -= 1

               
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best_len == float('inf'):
            return ""

        return s[best_left:best_left + best_len]