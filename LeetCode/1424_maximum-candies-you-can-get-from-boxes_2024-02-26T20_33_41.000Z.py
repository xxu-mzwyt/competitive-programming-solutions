# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        n = len(status)
        haveBox = [False] * n
        haveKey = [False] * n
        opened = [False] * n
        rslt = [0] * 1

        def openBox(label: int):
            opened[label] = True
            for key in keys[label]:
                haveKey[key] = True
            for box in containedBoxes[label]:
                haveBox[box] = True
            rslt[0] += candies[label]

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
                        openBox(i)
                        updated = True               

        return rslt[0]