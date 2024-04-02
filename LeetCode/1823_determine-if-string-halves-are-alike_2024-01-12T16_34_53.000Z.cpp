// https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution {
public:
    bool isVowel(char c) {
        string vowels = "aeiouAEIOU";
        const int NUM_VOWELS = 10;
        for (int i = 0; i < NUM_VOWELS; i++) {
            if (c == vowels[i]) {
                return true;
            }
        }
        return false;
    }
    bool halvesAreAlike(string s) {
        int l = s.length();
        int vowelsLeft = 0, vowelsRight = 0;
        for (int i = 0; i < l / 2; i++ ) {
            if (isVowel(s[i])) {
                vowelsLeft++;
            }
        }
        for (int i = l / 2; i < l; i++ ) {
            if (isVowel(s[i])) {
                vowelsRight++;
            }
        }
        return vowelsLeft == vowelsRight;
    }
};