# https://leetcode.com/problems/count-number-of-homogenous-substrings

class Solution:
    def countHomogenous(self, s: str) -> int:
        sumH = len(s)
        last = None
        sumCurr = 0
        for ch in s:
            if ch != last:
                sumH += sum(range(sumCurr))
                sumCurr = 1
            else:
                sumCurr += 1
            last = ch
        sumH += sum(range(sumCurr))
        return sumH % 1000000007
            