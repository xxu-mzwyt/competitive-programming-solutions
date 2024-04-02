# https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = 0
        for ch in s:
            if s.count(ch) == 1:
                return index
            index += 1
        return -1