# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        diffX = abs(fx - sx)
        diffY = abs(fy - sy)
        if diffX == 0 and diffY == 0:
            return t != 1
        if diffX > diffY:
            diffX, diffY = diffY, diffX
        return diffY <= t
        

        