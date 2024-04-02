# https://leetcode.com/problems/daily-temperatures

import heapq

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        num_days = len(temperatures)
        answer = [0] * num_days
        unresolved = []

        for i in range(num_days):
            curr = temperatures[i]
            while unresolved and curr > unresolved[0][0]:
                temp, index = heapq.heappop(unresolved)
                answer[index] = i - index
            heapq.heappush(unresolved, (temperatures[i], i))
        
        return answer