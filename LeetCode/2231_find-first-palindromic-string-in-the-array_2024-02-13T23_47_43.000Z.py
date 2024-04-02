# https://leetcode.com/problems/find-first-palindromic-string-in-the-array

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for wd in words:
            if wd == wd[::-1]:
                return wd
        return ""
        