# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(None)

        last = nums[0]
        maxCombo = -1
        currCombo = -1
        maxNum = None
        for num in nums:
            if num != last:
                if currCombo > maxCombo:
                    maxCombo = currCombo
                    maxNum = last
                last = num
                currCombo = 1
            else:
                currCombo += 1

        return maxNum


        