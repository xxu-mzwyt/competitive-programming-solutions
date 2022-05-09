m, n = map(int, input().split());

schools= list(map(int, input().split()));
students = list(map(int, input().split()));

rslt = 0

schools.sort()
students.sort()

curr = 0
for stu in students:
    while curr < m and schools[curr] < stu:
        curr += 1
    if curr == 0:
        rslt += schools[0] - stu
    elif curr == m:
        rslt += stu - schools[-1]
    else:
        rslt += min(schools[curr] - stu, stu - schools[curr - 1])

print(rslt)

# for stu in students:
#     schools.append(stu)
#     schools.sort()
#     stu_index = schools.index(stu)
#     if stu_index == 0:
#         rslt += schools[1] - stu
#     elif stu_index == m:
#         rslt += stu - schools[-2]
#     else:
#         rslt += min(stu - schools[stu_index - 1], schools[stu_index + 1] - stu)
#     # print(schools)
#     # print('rslt =', rslt)
#     schools.remove(stu)
# 
# print(rslt)
