// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int rslt = 0;
        int curr = 0;
        for (int i = 0; i < nums.size(); i++) {
            int next = i + 1;
            if (next == nums.size() || nums[i] != nums[next]) {
                nums[curr++] = nums[i];
                rslt++;
            }
        }
        return rslt;
    }
};