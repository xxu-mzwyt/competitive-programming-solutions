# https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        countPali = 0
        for i in range(len(s)):
            # palindromic substrings w/ odd length, centred at i
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                countPali += 1
            # now w/ even length, centred at i and i + 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                countPali += 1
        return countPali

        