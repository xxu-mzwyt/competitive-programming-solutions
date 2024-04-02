# https://leetcode.com/problems/palindromic-substrings

class Solution:
    def checkPali(self, s: str) -> bool:
        return s == s[::-1]
    def countSubstrings(self, s: str) -> int:
        countPali = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.checkPali(s[i:j]):
                    countPali += 1
        return countPali

        