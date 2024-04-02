// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        for(int i = 0; i < numbers.Length - 1; i++) {
            int currTarget = target - numbers[i];
            if (numbers[i] > currTarget) {
                break;
            }
            for (int j = i + 1; j < numbers.Length; j++) {
                if (numbers[j] == currTarget) {
                    return [i + 1, j + 1];
                }
            }
        }
        return [-1];
    }
}