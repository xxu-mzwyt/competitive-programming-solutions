# https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        freq_order = sorted(freq.keys(), key=lambda ch: freq[ch], reverse=True)
        return sum([[ch] * freq[ch] for ch in freq_order], [])
        