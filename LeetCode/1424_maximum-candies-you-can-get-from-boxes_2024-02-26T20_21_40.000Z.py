# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        n = len(status)
        haveBox = [False] * n
        haveKey = [False] * n
        opened = [False] * n
        for box in initialBoxes:
            haveBox[box] = True
        for i in range(n):
            haveKey[i] = bool(status[i] == 1)

        updated = True
        while updated:
            updated = False
            for i in range(n):
                if haveBox[i] and haveKey[i]:
                    if not opened[i]:
                        opened[i] = True
                        for key in keys[i]:
                            haveKey[key] = True
                        for box in containedBoxes[i]:
                            haveBox[box] = True
                        updated = True               

        rslt = 0
        for i in range(n):
            if opened[i]:
                rslt += candies[i]
        return rslt