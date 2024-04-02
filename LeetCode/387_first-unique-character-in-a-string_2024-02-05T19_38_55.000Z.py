# https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        index = 0
        for ch in s:
            if freq[ord(ch) - ord('a')] == 1:
                return index
            index += 1
        return -1