# from queue import Queue
from collections import deque

MAXK = 100000 + 1
HOURS24 = 86400

nati = [0] * MAXK
q = deque()

n = int(input().strip())
curr_nati = 0
for i in range(n):
    boat = list(map(int, input().split()))
    t, k = boat[0], boat[1]
    for i in boat[2:]:
        if nati[i] == 0:
            curr_nati += 1
        nati[i] += 1
    while len(q) > 0 and q[0][0] <= t - HOURS24:
        old_boat = q.popleft()
        for i in old_boat[2:]:
            nati[i] -= 1
            if nati[i] == 0:
                curr_nati -= 1
    # print("nati", nati[:5])
    q.append(boat)
    print(curr_nati)
