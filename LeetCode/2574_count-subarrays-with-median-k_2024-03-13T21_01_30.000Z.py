# https://leetcode.com/problems/count-subarrays-with-median-k

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        smaller = [0]
        greater = [0]
        smallerCnt = greaterCnt = 0
        # smaller/greater[i]: the number of elements that smaller or greater than k in nums[:i]
        kInd = -1
        for i in range(n):
            if nums[i] < k:
                smallerCnt += 1
            elif nums[i] > k:
                greaterCnt += 1
            else:
                kInd = i
            smaller.append(smallerCnt)
            greater.append(greaterCnt)
        rsltCnt = 1
        matchSG = {}
        for i in range(kInd + 2, n + 1): # considering [kInd + 1, i)
            smallerRange = smaller[i] - smaller[kInd + 1]
            greaterRange = greater[i] - greater[kInd + 1]
            diffRange = greaterRange - smallerRange
            if diffRange == 0 or diffRange == 1:
                rsltCnt += 1
            if diffRange in matchSG:
                matchSG[diffRange] += 1
            else:
                matchSG[diffRange] = 1
        print(matchSG)
        for i in range(0, kInd): # considering [i, kInd)
            smallerRange = smaller[kInd] - smaller[i]
            greaterRange = greater[kInd] - greater[i]
            diffRange = greaterRange - smallerRange
            if diffRange == 0 or diffRange == 1:
                rsltCnt += 1
            if 0 - diffRange in matchSG:
                rsltCnt += matchSG[0 - diffRange]
            if 1 - diffRange in matchSG:
                rsltCnt += matchSG[1 - diffRange]
        return rsltCnt

            

        