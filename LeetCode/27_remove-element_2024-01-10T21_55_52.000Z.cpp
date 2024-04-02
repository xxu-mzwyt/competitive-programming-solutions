// https://leetcode.com/problems/remove-element

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int tail = nums.size();
        int head = 0;
        int cnt = 0;
        while (head < tail) {
            if (nums[head] != val) {
                head++;
                cnt++;
            }
            else {
                tail--;
                nums[head] = nums[tail];
            }
        }
        return cnt;
    }
};