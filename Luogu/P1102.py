n, c = map(int, input().split())
num_arr = list(map(int, input().split()))

num_arr.sort()
counted_arr = []

curr_val = num_arr[0]
curr_cnt = 0
for i in num_arr:
    if i == curr_val:
        curr_cnt += 1
    else:
        counted_arr.append((curr_val, curr_cnt))
        curr_val = i
        curr_cnt = 1
counted_arr.append((curr_val, curr_cnt))
num_arr = counted_arr
n = len(num_arr)

rslt = 0

# for i in num_arr:
#     for j in num_arr:
#         if i - j == c:
#             rslt += 1

# 1 2 3 8 10 18
# 10

curr = 0
last = 0
while curr < n:
    if num_arr[curr][0] - num_arr[last][0] < c:
        curr += 1
    elif num_arr[curr][0] - num_arr[last][0] > c:
        last += 1 
    else:
        # print(last, curr)
        rslt += num_arr[curr][1] * num_arr[last][1]
        curr += 1

print(rslt)
