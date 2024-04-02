# https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losts = []
        NUM_PLAYER = 100005
        for i in range(NUM_PLAYER):
            losts.append(-1)
        for match in matches:
            if losts[match[0]] < 0:
                losts[match[0]] = 0
            if losts[match[1]] < 0:
                losts[match[1]] = 0
            losts[match[1]] += 1
        lost0 = []
        lost1 = []
        for i in range(NUM_PLAYER):
            if losts[i] == 0:
                lost0.append(i)
            elif losts[i] == 1:
                lost1.append(i)
        return [lost0, lost1]
        
        