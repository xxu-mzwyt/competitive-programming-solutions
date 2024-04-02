# https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive = [i for i in nums if i > 0]
        n = len(positive)
        for i in range(n):
            index = abs(positive[i]) - 1
            if index >= 0 and index < n:
                positive[index] = 0 - abs(positive[index])
        for i in range(n):
            if positive[i] > 0:
                return i + 1
        return n + 1

        