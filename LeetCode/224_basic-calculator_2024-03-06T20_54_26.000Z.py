# https://leetcode.com/problems/basic-calculator

class Solution:
    def calculate(self, s: str) -> int:
        def calculateLst(lst) -> int:
            if type(lst) == str:
                return int(lst)
            elif not lst:
                return 0
            elif lst[0] == "+":
                return calculateLst(lst[1]) + calculateLst(lst[2:])
            elif lst[0] == "-":
                return - calculateLst(lst[1]) + calculateLst(lst[2:])
            else:
                return calculateLst(lst[0]) + calculateLst(lst[1:])
        def convertLst(s: str):
            sl = []
            curr = 0
            while curr < len(s):
                ch = s[curr]
                if ch == "(":
                    braExp, braLen = convertLst(s[curr + 1:])
                    sl.append(braExp)
                    curr += braLen
                elif ch == ")":
                    return sl, curr + 1
                elif ch.isdigit() and sl and sl[-1].isdigit():
                    sl[-1] += ch
                elif ch != " ":
                    sl.append(ch)
                curr += 1
            return sl
        return calculateLst(convertLst(s))
        