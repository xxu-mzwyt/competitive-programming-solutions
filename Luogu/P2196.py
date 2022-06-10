n = int(input().strip())

mine_cnt = list(map(int, input().split()))
paths = []

for i in range(n):
    paths.append([0] * (i + 1))
    if i < n - 1:
        paths[i].extend(list(map(int, input().split())))

max_mine = [0] * n

for i in range(n - 1, -1, -1):
    curr_max_mine = 0
    curr_max_path = []
    for j in range(i + 1, n):
        if paths[i][j] and max_mine[j][0] > curr_max_mine:
            curr_max_mine = max_mine[j][0]
            curr_max_path = max_mine[j][1]
    max_mine[i] = (mine_cnt[i] + curr_max_mine, [i + 1] + curr_max_path)

print(*max(max_mine)[1])
print(max(max_mine)[0])
                


