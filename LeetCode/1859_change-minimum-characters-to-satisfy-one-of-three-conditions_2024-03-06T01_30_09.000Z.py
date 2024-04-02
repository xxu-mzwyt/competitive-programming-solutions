# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        incA = [ord(ch) - ord('a') for ch in sorted(a)]
        incB = [ord(ch) - ord('a') for ch in sorted(b)]
        minRslt = 200001
        for i in range(25):
            smallerA = 0
            for j in range(len(a)):
                if incA[j] > i:
                    break
                smallerA = j + 1
            largerA = len(a) - smallerA
            smallerB = 0
            for j in range(len(b)):
                if incB[j] > i:
                    break
                smallerB = j + 1
            largerB = len(b) - smallerB
            minRslt = min(minRslt, smallerA + largerB, smallerB + largerA)

        modeA = a.count(max(set(a), key=a.count))
        modeB = b.count(max(set(b), key=b.count))
        minRslt = min(minRslt, len(a) - modeA + len(b) - modeB)             
            
        return minRslt

        