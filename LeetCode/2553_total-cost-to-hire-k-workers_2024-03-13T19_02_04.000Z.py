# https://leetcode.com/problems/total-cost-to-hire-k-workers

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        import heapq
        n = len(costs)
        left = []
        right = []
        leftNext = 0
        rightNext = n - 1
        for _ in range(candidates):
            if leftNext <= rightNext:
                heapq.heappush(left, costs[leftNext])
                leftNext += 1
            if leftNext <= rightNext:
                heapq.heappush(right, costs[rightNext])
                rightNext -= 1
        sumCost = 0
        for i in range(k):
            leftMin = rightMin = 100001
            if left:
                leftMin = left[0]
            if right:
                rightMin = right[0]
            if leftMin <= rightMin:
                sumCost += leftMin
                heapq.heappop(left)
                if leftNext <= rightNext:
                    heapq.heappush(left, costs[leftNext])
                    leftNext += 1
            else:
                sumCost += rightMin
                heapq.heappop(right)
                if leftNext <= rightNext:
                    heapq.heappush(right, costs[rightNext])
                    rightNext -= 1
        return sumCost