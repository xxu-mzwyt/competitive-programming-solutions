# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends

class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r and s[l] == s[r]:  # if len == 1 stop (cannot have intersection)
            ch = s[l]
            while l <= r and s[l] == ch:  # we can continue until len == 0 (same char)
                l += 1
            while l <= r and s[r] == ch:
                r -= 1
        return r - l + 1
        