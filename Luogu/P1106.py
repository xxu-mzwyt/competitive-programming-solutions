num = list(map(int, input().strip()))
k = int(input().strip())

m = len(num) - k
rslt = []

lb = 0
ub = k + 1

for i in range(m):
    avl = num[lb:ub]
    curr = avl.index(min(avl)) + lb
    rslt.append(num[curr])
    lb = curr + 1
    ub += 1

rslt = "".join(map(str, rslt)).lstrip("0")
if not rslt:
    print(0)
else:
    print(rslt)

