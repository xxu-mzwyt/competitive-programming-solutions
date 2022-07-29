while True:
    
    try:
        n, m = map(int, input().split())
    except ValueError:
        break
    
    parent = []
    for i in range(n + 1):
        parent.append(i)

    def find(x, prt):
        if prt[x] == x:
            return x
        else:
            prt[x] = find(prt[x], prt)
            return prt[x]

    def merge(x, y, prt):
        x_p = find(x, prt)
        y_p = find(y, prt)
        if x_p == y_p:
            return 0
        else:
            prt[x_p] = y_p
            return -1
    
    groups_cnt = n - 1
    for _ in range(m):
        a, b = map(int, input().split())
        groups_cnt += merge(a, b, parent)
        # a_p = find(a, parent)
        # b_p = find(b, parent)
        # if a_p == b_p:
        #     continue
        # else:
        #     parent[a_p] = b_p
        #     groups_cnt -= 1

    print(groups_cnt)
