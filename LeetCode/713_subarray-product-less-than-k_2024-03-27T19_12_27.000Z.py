# https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = 0
        rslt = 0
        curr = 1
        while r < n:
            if curr >= k:
                l += 1
                r += 1
            # print("new cycle at", l, r)
            while curr < k and r < n:
                # print(l, r, curr)
                rslt += (r - l)
                curr *= nums[r]
                r += 1
            while curr >= k and l < r:
                # print(l, r)
                curr //= nums[l]
                l += 1
        rslt += (r - l)
        return rslt
    """
    10, 5, 2, 6
    0, 0
    0, 1 [10] + 1
    0, 2 [10, 5] + 2
    0, 3 [10, 5, 2]
    1, 3 [5, 2] + 2
    1, 4 [5, 2, 6] + 3
    """





                


        