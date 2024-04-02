# https://leetcode.com/problems/minimum-window-substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        unfilled = 0
        for ch in t:
            if ch not in freq:
                unfilled += 1
                freq[ch] = 1
            else:
                freq[ch] += 1
        l = 0
        r = 0
        minLen = 100001
        minStr = ""
        while r < len(s):
            print(l, r)
            while unfilled > 0 and r < len(s):
                if s[r] in freq:
                    freq[s[r]] -= 1
                    if freq[s[r]] == 0:
                        unfilled -= 1
                r += 1
            while unfilled <= 0 and l < r:
                if r - l < minLen:
                    minLen = r - l
                    minStr = s[l:r]
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] == 1:
                        unfilled += 1
                l += 1

        return minStr

            



        