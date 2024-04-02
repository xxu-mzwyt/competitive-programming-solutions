# https://leetcode.com/problems/task-scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            if t in freq:
                freq[t] += 1
            else:
                freq[t] = 1
        tasksFreq = list(freq.values())
        return max(sum(tasksFreq), (max(tasksFreq) - 1) * (n + 1) + tasksFreq.count(max(tasksFreq)))
        
          
        