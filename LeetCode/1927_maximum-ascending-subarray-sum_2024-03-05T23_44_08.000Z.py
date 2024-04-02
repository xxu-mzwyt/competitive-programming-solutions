# https://leetcode.com/problems/maximum-ascending-subarray-sum

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        last = -1
        maxSum = -1
        currSum = 0
        for n in nums:
            if n > last:
                currSum += n
            else:
                if currSum > maxSum:
                    maxSum = currSum
                currSum = n
            last = n
        return max(maxSum, currSum)


        