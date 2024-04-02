# https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        NUM_PLAYER = 100005
        losses = [-1] * NUM_PLAYER
        for match in matches:
            if losses[match[0]] < 0:
                losses[match[0]] = 0
            if losses[match[1]] < 0:
                losses[match[1]] = 0
            losses[match[1]] += 1
        
        lost0 = []
        lost1 = []
        for i in range(NUM_PLAYER):
            if losses[i] == 0:
                lost0.append(i)
            elif losses[i] == 1:
                lost1.append(i)
        return [lost0, lost1]
        
        