# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s = [ord(ch) for ch in s]
        t = [ord(ch) for ch in t]
        n = len(s)
        for i in range(n):
            source = s[i]
            target = t[i]
            if source == -1 and target == -1:
                continue
            for j in range(n):
                if s[j] == source and t[j] == target:
                    s[j] = t[j] = -1
                elif s[j] != source and t[j] != target:
                    continue
                else:
                    return False                
        return True



        