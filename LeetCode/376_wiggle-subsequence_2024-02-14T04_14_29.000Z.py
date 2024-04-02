# https://leetcode.com/problems/wiggle-subsequence

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        last = nums[0]
        currLen = 1
        isRising = None
        for curr in nums[1:]:
            if curr == last:
                continue
            elif (curr > last) != isRising:
                isRising = (curr > last)
                last = curr
                currLen += 1
            else:
                # same rise/fall as before, take newer (more extreme) one by greedy
                last = curr
        return currLen


            