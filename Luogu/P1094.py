w = int(input().strip())
n = int(input().strip())

gifts = []
for i in range(n):
    gifts.append(int(input().strip()))
gifts.sort()
# print(gifts)

groups_cnt = 0

l = 0
r = n - 1

while l < r:
    if gifts[l] + gifts[r] > w:
        r -= 1
    else:
        l += 1
        r -= 1
    groups_cnt += 1
    # print("l, r =", l, r)
    # print("g[l], g[r] =", gifts[l], gifts[r])

if l == r:
    groups_cnt += 1

print(groups_cnt)
