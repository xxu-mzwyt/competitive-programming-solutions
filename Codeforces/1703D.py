t = int(input().strip())

for _ in range(t):
    
    n = int(input().strip())

    s = []
    sdic = {}
    
    for _ in range(n):
        si = input().strip()
        s.append(si)
        sdic[si] = True

    for i in s:
        exist = 0
        for j in range(1, len(i)):
            if i[:j] in sdic and i[j:] in sdic:
                exist = 1
                break
        print(exist, end='')

    print() 

