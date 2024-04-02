# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ORD_A = ord('a')
        NUM_LETTERS = 26
        lettersFreqS = [0] * NUM_LETTERS
        for char in s:
            ordChar = ord(char) - ORD_A
            lettersFreqS[ordChar] += 1
        for char in t:
            ordChar = ord(char) - ORD_A
            if lettersFreqS[ordChar] > 0:
                lettersFreqS[ordChar] -= 1
        return sum(lettersFreqS)