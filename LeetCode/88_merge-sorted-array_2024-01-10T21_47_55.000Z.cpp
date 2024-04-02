// https://leetcode.com/problems/merge-sorted-array

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> rslt;
        int a = 0, b = 0;
        while (a < m && b < n) {
            if (nums1[a] < nums2[b]) {
                rslt.push_back(nums1[a++]);
            }
            else {
                rslt.push_back(nums2[b++]);
            }
        }
        for (; a < m; a++) {
            rslt.push_back(nums1[a]);
        }
        for (; b < n; b++) {
            rslt.push_back(nums2[b]);
        }
        nums1 = rslt;
    }
};