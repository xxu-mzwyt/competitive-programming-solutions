n = int(input().strip())

appeared = {}
rslt = 0

for _ in range(n):
    s = input().strip()
    if s in appeared:
        continue
    else:
        appeared[s] = True
        rslt += 1

print(rslt)
