n, m, b, g = map(int, input().split())

rows = [0] * (n + 1) 
cols = [0] * (m + 1)

for i in range(b):
    x, y = map(int, input().split())
    # for j in range(x, y+1):
    #     if rows[j - 1] == 0:
    #         rows[j - 1] = 1
    #         num_rows += 1
    rows[x - 1] += 1
    rows[y] -= 1


for i in range(g):
    x, y = map(int, input().split())
    # for j in range(x, y+1):
    #     if cols[j - 1] == 0:
    #         cols[j - 1] = 1
    #         num_cols += 1
    cols[x - 1] += 1
    cols[y] -= 1


num_rows = 0
num_cols = 0

curr = 0
for i in rows:
    curr += i
    if curr > 0:
        num_rows += 1

curr = 0
for i in cols:
    curr += i
    if curr > 0:
        num_cols += 1

# def intersect(x, y):
#     if y[0] < x[0]:
#         x, y = y, x
#     if y[0] > x[1]:
#         return 0
#     elif y[1] <= x[1]:
#         return y[1] - y[0] + 1
#     else:
#         return y[0] - x[1] + 1 


# for i in range(b):
#     for j in range(i + 1, b):
#         num_rows -= intersect(rows[i], rows[j])

# for i in range(g):
#     for j in range(i + 1, g):
#         num_cols -= intersect(cols[i], cols[j])

# def comp(x1, x2):
#     return x1[0] < x2[0]

# rows.sort(key = lambda x : (x[0], x[1]))
# cols.sort(key = lambda x : (x[0], x[1]))

# rows_merged = [rows[0]]
# cols_merged = [cols[0]]

# for i in rows[1:]:
#     if i[0] <= rows_merged[-1][1]:
#         rows_merged[-1] = ((rows_merged[-1][0], max(i[1], rows_merged[-1][1])))
#     else:
#         rows_merged.append(i)

# for i in cols[1:]:
#     if i[0] <= rows_merged[-1][1]:
#         cols_merged[-1] = ((cols_merged[-1][0], max(i[1], cols_merged[-1][1])))
#     else:
#         cols_merged.append(i)


# for i in rows_merged:
#     num_rows += i[1] - i[0] + 1

# for i in cols_merged:
#     num_cols += i[1] - i[0] + 1

# print(num_rows, num_cols)

print(num_rows * m + num_cols * n - num_rows * num_cols)