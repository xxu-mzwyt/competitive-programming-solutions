// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        for(int i = 0; i < numbers.Length - 1; i++) {
            int currTarget = target - numbers[i];
            if (numbers[numbers.Length - 1] < currTarget) {
                continue;
            }
            if (numbers[i] > currTarget) {
                break;
            }
            int l = i + 1;
            int r = numbers.Length;
            while (l < r) {
                int mid = (l + r) / 2;
                int curr = numbers[mid];
                if (curr == currTarget) {
                    return [i + 1, mid + 1];
                }
                else if (curr < currTarget) {
                    l = mid + 1;
                }
                else {
                    r = mid;
                }
            }
        }
        return [];
    }
}