# https://leetcode.com/problems/determine-if-two-strings-are-close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        ORD_A = ord('a')
        NUM_LETTERS = 26

        lettersFreq1 = [0] * NUM_LETTERS
        lettersFreq2 = [0] * NUM_LETTERS
        for char in word1:
            charOrd = ord(char) - ORD_A
            lettersFreq1[charOrd] += 1
        for char in word2:
            charOrd = ord(char) - ORD_A
            lettersFreq2[charOrd] += 1

        for i in range(NUM_LETTERS):
            if bool(lettersFreq1[i]) !=  bool(lettersFreq2[i]):
                return False
                
        return sorted(lettersFreq1) == sorted(lettersFreq2)