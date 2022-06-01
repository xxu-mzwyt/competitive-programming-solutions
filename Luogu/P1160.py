n = int(input().strip())

# queue = [1]
# for i in range(2, n + 1):
#     k, p = map(int, input().split())
#     queue.insert(queue.index(k) + p, i)
# 
# m = int(input().strip())
# for i in range(m):
#     try:
#         queue.remove(int(input().strip()))
#     except:
#         pass
# 
# print(*queue, sep=' ')

queue = [[1, 1]]
for i in range(n):
    queue.append([0, 0])

for i in range(2, n + 1):
    k, p = map(int, input().split())
    e = (1, 0)[p]
    queue[i][p] = queue[k][p]
    queue[i][e] = k
    queue[k][p] = i
    queue[queue[i][p]][e] = i

m = int(input().strip())

for i in range(m):
    r = int(input().strip())
    if queue[r][0] + queue[r][1] == 0:
        continue
    queue[queue[r][0]][1] = queue[r][1]
    queue[queue[r][1]][0] = queue[r][0]
    queue[r] = [0, 0]

curr = queue[0][1]
while curr != 0:
    print(curr, end=' ')
    curr = queue[curr][1]
