// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int rslt = 0;
        int curr = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int next2 = i + 2;
            if (next2 >= n || nums[i] != nums[next2]) {
                nums[curr++] = nums[i];
                rslt++;
            }
        }
        return rslt;
    }
};