l, n, m = map(int, input().split())

dis = []

last = 0
for i in range(n):
    curr = int(input())
    dis.append(curr - last)
    last = curr
dis.append(l - last)

# print(dis)

lb = 0
ub = l + 1

def remove_stone(th):
    
    removed_cnt = 0
    curr = 0

    for i in dis:
        curr += i
        if curr < th:
            removed_cnt += 1
            if removed_cnt > m:
                return False
        else:
            curr = 0

    return True

while ub - lb > 1:
    mid = (ub + lb) // 2
    # print('curr mid is', mid) 
    if not remove_stone(mid):
        ub = mid
    else:
        lb = mid

print(lb)     
