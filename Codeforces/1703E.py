t = int(input().strip())

for _ in range(t):
    
    n = int(input().strip())
    
    mp = []
    # vis = list(map(lambda x: [0] * 5, [0] * 5))

    rslt = 0

    for _ in range(n):
        mp.append(list(input().strip()))

    for i in range(n // 2):
        for j in range((n + 1) // 2):
            zeros = 0
            ones = 0
            for cood in [(i, j), (j, n - i - 1), (n - i - 1, n - j - 1), (n - j - 1, i)]:
                # vis[cood[0]][cood[1]] += 1
                # print(*vis, sep='\n')
                # print()
                if mp[cood[0]][cood[1]] == '0':
                    zeros += 1
                else:
                    ones += 1
            rslt += min(zeros, ones)
    print(rslt)

# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

