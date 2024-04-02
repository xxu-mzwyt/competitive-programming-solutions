# https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        MAX_NUM = 1000
        freq = [0] * (MAX_NUM * 2 + 1)
        for i in arr:
            freq[i + MAX_NUM] += 1
        freq = [i for i in freq if i > 0]
        return len(set(freq)) == len(freq)