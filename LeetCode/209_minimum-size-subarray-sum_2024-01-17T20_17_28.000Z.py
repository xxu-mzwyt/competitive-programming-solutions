# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        end = len(nums)
        currSum = 0
        minLen = 0
        while right < end:
            while right < end and currSum < target:
                currSum += nums[right]
                right += 1
            print("right to", right)
            print("sum is", currSum)
            while currSum >= target:
                if minLen == 0 or right - left < minLen:
                    minLen = right - left
                currSum -= nums[left]
                left += 1
            print("left to", left)
            print("sum reduced to", currSum)
        return minLen