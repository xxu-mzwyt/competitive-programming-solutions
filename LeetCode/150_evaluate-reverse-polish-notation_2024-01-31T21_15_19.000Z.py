# https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        curr = tokens.pop()
        if curr in ["+", "-", "*", "/"]:
            opr2 = self.evalRPN(tokens)
            opr1 = self.evalRPN(tokens)
            if curr == "+":
                return opr1 + opr2
            elif curr == "-":
                return opr1 - opr2
            elif curr == "*":
                return opr1 * opr2
            elif curr == "/":
                return int(opr1 / opr2)
        else:
            return int(curr)
        