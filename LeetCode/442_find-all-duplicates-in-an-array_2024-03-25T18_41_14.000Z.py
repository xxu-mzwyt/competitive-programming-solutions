# https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        MAX_NUM = 100001
        appeared = [False] * MAX_NUM
        duplicated = []
        for num in nums:
            if appeared[num]:
                duplicated.append(num)
            else:
                appeared[num] = True
        return duplicated

        