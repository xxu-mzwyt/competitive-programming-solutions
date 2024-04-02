# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        rslt = []
        currDiff = sum(nums)
        last = 0
        for i in range(len(nums)):
            diff = nums[i] - last
            if diff > 0:
                currDiff = currDiff + (i) * diff - (len(nums) - i) * diff
            rslt.append(currDiff)
            last = nums[i]
        return rslt
        