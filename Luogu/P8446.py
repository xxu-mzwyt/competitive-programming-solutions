n = int(input().strip())
a = input().split()

curr_max = float("-inf")
curr_min = float("+inf")

max_rslt = float("-inf")

for i in a:

    curr = int(i)

    curr_max = max(curr_max, curr)
    curr_min = min(curr_min, curr)

    curr_max -= 1
    curr_min += 1

    max_rslt = max(max_rslt, curr_max - curr, curr - curr_min)

print(max_rslt)
