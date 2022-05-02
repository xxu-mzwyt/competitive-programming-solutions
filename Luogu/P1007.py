l = int(input())
n = int(input())

if n == 0:
    print(0, 0)
else:
    pos = map(int, input().split())

    min_t = -1
    max_t = -1

    for i in pos:
        if min(i, l + 1 - i) > min_t:
            min_t = min(i, l + 1 - i)
        if max(i, l + 1 - i) > max_t:
            max_t = max(i, l + 1 - i)

    print(min_t, max_t)
