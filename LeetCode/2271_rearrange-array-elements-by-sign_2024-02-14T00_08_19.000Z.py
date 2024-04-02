# https://leetcode.com/problems/rearrange-array-elements-by-sign

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        rslt = []
        for i in range(len(pos)):
            rslt.append(pos[i])
            rslt.append(neg[i])
        return rslt


        