n, k = map(int, input().split())

# L = list(map(int, input().split()))

L = []
for i in range(n):
    L.append(int(input()))

lb = 0
ub = int(1e8) + 1

def cut(slen):
    sum = 0
    for i in L:
        sum += i // slen
    return sum >= k 

while ub - lb > 1: 
    mid = (lb + ub) // 2
    if cut(mid):
        lb = mid
    else:
        ub = mid
    # print('upper', ub, 'lower', lb)

print(lb)
