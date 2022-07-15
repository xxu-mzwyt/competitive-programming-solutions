t = int(input().strip())

for _ in range(t):

    n, c, q = map(int, input().split())
    s = input().strip()
   
    currLen = n

    seg = [(0, currLen, 0)] # [lowerbound, upperbound), start(l)

    def find_orgn(sg, x):
        for i in sg:
            if i[1] > x:
                return i[2] + x - i[0]

    for _ in range(c):
        l, r = map(lambda x: int(x) - 1, input().split())
        seg.append((currLen, currLen + r - l + 1, l))
        currLen += r - l + 1

    # print(seg)
    # for i in range(currLen):
    #     k = i
    #     while k >= n:
    #         k = find_orgn(seg, k)
    #     print(s[k], end='')
    # print()

    for _ in range(q):
        k = int(input().strip()) - 1
        while k >= n:
            k = find_orgn(seg, k)
        print(s[k])

