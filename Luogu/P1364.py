dis = []
wt = []

n = int(input().strip())
for i in range(n):
    dis.append([float("inf")] * n)
    dis[i][i] = 0
for i in range(n):
    w, l, r = map(int, input().split())
    wt.append(w)
    if l:
        dis[i][l - 1] = dis[l - 1][i] = 1
    if r:
        dis[i][r - 1] = dis[r - 1][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dis[i][k] + dis[k][j] < dis[i][j]:
                dis[i][j] = dis[i][k] + dis[k][j]

min_dis = float("inf")
min_idx = 0
for i in range(n):
    dis_sum = 0
    for j in range(n):
        dis_sum += dis[j][i] * wt[j]
    if dis_sum < min_dis:
        min_dis = dis_sum
        min_idx = i + 1

ziped_dis = map(lambda x: zip(x, wt), dis)
muled_dis = map(lambda x: sum(map(lambda y: y[0] * y[1], x)), ziped_dis)

print(min(muled_dis))

