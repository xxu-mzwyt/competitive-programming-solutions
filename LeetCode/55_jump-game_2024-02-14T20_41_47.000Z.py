# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        pos = 1  # skipped [0] since we only need to reach the end
        while pos < len(nums):
            if nums[pos] <= 0:
                jumped = False
                for j in range(pos + 1, len(nums)):
                    if nums[j] > j - pos:
                        pos = j
                        jumped = True
                        break
                if not jumped:
                    return False
            else:
                pos += 1
        return True
        