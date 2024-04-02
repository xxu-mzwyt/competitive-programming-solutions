# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strFreqs = []
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            strFreqs.append((freq, s))
        strFreqs.sort()
        last = None
        curr = []
        groups = []
        for freq, s in strFreqs:
            if freq != last:
                groups.append(curr)
                curr = [s]
            else:
                curr.append(s)
            last = freq
        groups.append(curr)
        return groups[1:]
        