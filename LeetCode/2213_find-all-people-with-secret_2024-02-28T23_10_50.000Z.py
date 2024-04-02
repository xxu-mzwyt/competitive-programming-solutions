# https://leetcode.com/problems/find-all-people-with-secret

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        knowSecret = [False] * n
        knowSecret[0] = knowSecret[firstPerson] = True
        meetings.sort(key=lambda lst : lst[2])
        currMeetings = []
        currTime = None
        
        def spreadSecret(curr):
            updated = True
            while updated:
                updated = False
                for x, y in curr:
                    if knowSecret[x] and not knowSecret[y]:
                        knowSecret[y] = True
                        updated = True
                    if knowSecret[y] and not knowSecret[x]:
                        knowSecret[x] = True
                        updated = True 

        for x, y, time in meetings:
            if time != currTime:
                spreadSecret(currMeetings)
                currMeetings = []
                currTime = time
            currMeetings.append((x, y))
        spreadSecret(currMeetings)
        return [i for i in range(n) if knowSecret[i]]