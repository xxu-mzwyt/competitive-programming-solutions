n, m = map(int, input().split())

mat = []


def mark_mine(x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            nx, ny = x + i, y + j
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if mat[nx][ny] != '*':
                    mat[nx][ny] += 1


for i in range(n):
    mat.append(list(input()))

for i in range(n):
    for j in range(m):
        if mat[i][j] == '?':
            mat[i][j] = 0

for i in range(n):
    for j in range(m):
        if mat[i][j] == '*':
            mark_mine(i, j)

for i in range(n):
    for j in range(m):
        print(mat[i][j], end='')
    print()
