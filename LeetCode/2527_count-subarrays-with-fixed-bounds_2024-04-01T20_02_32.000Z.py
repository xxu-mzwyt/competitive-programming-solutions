# https://leetcode.com/problems/count-subarrays-with-fixed-bounds

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        rslt = 0

        """ O(n^2) solution
        for i in range(n):
            minExisted = maxExisted = False
            for j in range(i, n):
                if nums[j] == minK:
                    minExisted = True
                if nums[j] == maxK:
                    maxExisted = True
                if nums[j] < minK or nums[j] > maxK:
                    break
                if minExisted and maxExisted:
                    rslt += 1   
        return rslt 
        """

        maxWaiting = minWaiting = bothWaiting = noLongerWaiting = 0
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                maxWaiting = minWaiting = bothWaiting = noLongerWaiting = 0
                continue
            bothWaiting += 1
            if nums[i] == minK:
                noLongerWaiting += minWaiting
                minWaiting = 0
                maxWaiting += bothWaiting
                bothWaiting = 0
            if nums[i] == maxK:
                noLongerWaiting += maxWaiting
                maxWaiting = 0
                minWaiting += bothWaiting
                bothWaiting = 0
            rslt += noLongerWaiting
        return rslt

