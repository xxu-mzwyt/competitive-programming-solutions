r, c = map(int, input().split())

ht = []
vis = []
for i in range(r):
    ht.append(list(map(int, input().split())))
    vis.append([0] * c)

def ski(x, y):
    if vis[x][y] > 0:
        return vis[x][y]
    max_route = 1
    for d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        nx = x + d[0]
        ny = y + d[1]
        if nx < 0 or nx >= r:
            continue
        if ny < 0 or ny >= c:
            continue
        if ht[nx][ny] >= ht[x][y]:
            # print(nx, ny, "higher than", x, y)
            continue
        # print("from", x, y, "to", nx, ny)
        max_route = max(max_route, ski(nx, ny) + 1)
    vis[x][y] = max_route
    return max_route
    
for i in range(r):
    for j in range(c):
        ski(i, j)
max_rslt = max(map(max, vis))

print(max_rslt)

