n, c = map(int, input().split())

cells = []
for i in range(n):
    cells.append(int(input().strip()))
cells.sort()

lb = 0
ub = cells[n - 1]


def check_cells(th):
    curr_dis = cells[0]
    cows_cnt = 1
    for i in cells:
        if i - curr_dis >= th:
            curr_dis = i
            cows_cnt += 1
    # print("thd", th, "cnt", cows_cnt)
    if cows_cnt >= c:
        return True
    else:
        return False


while lb < ub - 1:
    mid = (ub + lb) // 2
    # print("current range:", lb, mid, ub)
    if check_cells(mid):
        lb = mid
    else:
        ub = mid

print(lb)
