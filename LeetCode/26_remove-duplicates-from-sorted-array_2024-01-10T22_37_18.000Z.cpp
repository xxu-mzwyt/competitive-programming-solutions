// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int rslt = 0;
        int curr = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int next = i + 1;
            if (next == n || nums[i] != nums[next]) {
                nums[curr++] = nums[i];
                rslt++;
            }
        }
        return rslt;
    }
};