n = int(input().strip())
price = list(map(int, input().split()))
w = int(input().strip())

price.sort(reverse = True)

chosen = -1
for i in price:
    if i <= w:
        chosen = i
        break

rslt = 0
for i in price[::-1]:
    if i <= chosen:
        rslt += 1
        chosen -= i
    else:
        break

print(rslt)
