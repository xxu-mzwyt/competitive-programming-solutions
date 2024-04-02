# https://leetcode.com/problems/find-the-pivot-integer

class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = sum(range(n + 1))
        for curr in range(0, n):
            left += curr + 1
            right -= curr
            if left == right:
                return curr + 1
            elif left > right:
                return -1

        