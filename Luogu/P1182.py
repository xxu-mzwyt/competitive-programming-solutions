n, m = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

lb = max(nums)
ub = sum(nums)

# print("ub, lb:", ub, lb)

def split_num(thd):
    curr = thd
    group_cnt = 1
    for i in nums:
        if curr < i:
            group_cnt += 1
            curr = thd
        curr -= i

    # print("spliting", thd, "rslt", group_cnt)
    return group_cnt

while ub >= lb:
    mid = (lb + ub) // 2
    if split_num(mid) > m:
        lb = mid + 1
    else:
        ub = mid - 1
    # print("ub, lb:", ub, lb)

print(lb)
