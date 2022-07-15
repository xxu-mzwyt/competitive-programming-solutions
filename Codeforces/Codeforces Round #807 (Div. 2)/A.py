t = int(input().strip())

for _ in range(t):

    n, x = map(int, input().split())
    h = list(map(int, input().split()))

    h.sort()
    # print(h)

    possible = True
    for i in range(n):
        if h[n + i] - h[i] < x:
            possible = False
            break

    if possible:
        print('YES')
    else:
        print('NO')

