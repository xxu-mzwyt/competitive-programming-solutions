t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    print(len(s) + len(set(s)))
