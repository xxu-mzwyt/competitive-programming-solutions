# https://leetcode.com/problems/create-maximum-number

class Solution:

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def findMax(arr, num):
            if num == 0:
                return []
            
            if num == 1:
                maxVal = max(arr)
            else:
                maxVal = max(arr[: 1 - num])

            maxIdx = arr.index(maxVal)
            arrRest = findMax(arr[maxIdx + 1:], num - 1)
            arrRest.insert(0, maxVal)
            return arrRest

        def merge(arr1, arr2):
            rslt = []
            while arr1 and arr2:
                if arr1 > arr2:
                    rslt.append(arr1.pop(0))
                else:
                    rslt.append(arr2.pop(0))
            rslt = rslt + arr1 + arr2
            return rslt

        kMax = [-1] * k
        for k1 in range(k + 1):
            k2 = k - k1
            if k1 > len(nums1):
                continue
            elif k2 > len(nums2):
                continue

            max1 = findMax(nums1, k1)
            max2 = findMax(nums2, k2)
            kCurr = merge(max1, max2)
            if kCurr > kMax:
                kMax = kCurr

        return kMax
        