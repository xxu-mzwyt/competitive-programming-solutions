# https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rslt = []
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                rslt.append(abs(nums[i]))
            else:
                nums[idx] = 0 - nums[idx]
        return rslt

            
        