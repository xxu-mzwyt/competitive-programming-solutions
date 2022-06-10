r = int(input().strip())

tri = []
for i in range(r):
    tri.append(list(map(int, input().split())))

for i in range(r - 2, -1, -1):
    for j in range(i + 1):
        tri[i][j] += max(tri[i + 1][j], tri[i + 1][j + 1])

print(tri[0][0])
