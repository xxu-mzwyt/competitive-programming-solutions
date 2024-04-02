// https://leetcode.com/problems/set-mismatch

public class Solution {
    public int[] FindErrorNums(int[] nums) {
        const int MAX_NUM = 10005;

        int twice = -1;
        int missing = -1;

        bool[] visited = new bool [MAX_NUM];

        foreach (int n in nums) {
            if (visited[n]) {
                twice = n;
            }
            visited[n] = true;
        }
        for (int i = 1; i <= nums.Length; i++) {
            if (!visited[i]) {
                missing = i;
            }
        }

        return [twice, missing];
    }
}