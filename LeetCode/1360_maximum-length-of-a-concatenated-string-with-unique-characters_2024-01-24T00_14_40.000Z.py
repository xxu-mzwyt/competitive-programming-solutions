# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

class Solution:
    def validAppend(self, arr: List[str], t: str) -> bool:
        def shareChar(s: str, t: str) -> bool:
            for c in s:
                if c in t:
                    return True
            return False
        if len(set(t)) < len(t):
            return False
        for s in arr:
            if shareChar(s, t):
                return False
        return True

    def maxLength(self, arr: List[str]) -> int:
        def findMaxLength(arr, rslt):
            if not arr:
                return sum(len(s) for s in rslt)

            if self.validAppend(rslt, arr[0]):
                rslt.append(arr[0])
                maxLengthWith = findMaxLength(arr[1:], rslt)
                rslt.pop()
            else:    
                maxLengthWith = -1
            maxLengthWithout = findMaxLength(arr[1:], rslt)

            return max(maxLengthWith, maxLengthWithout)

        return findMaxLength(arr, [])