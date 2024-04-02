// https://leetcode.com/problems/rotate-array

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        vector<int> rslt;
        for (int i = 0; i < n; i++) {
            rslt.push_back(nums[(i - k + n) % n]);
        }
        nums = rslt;
    }
};