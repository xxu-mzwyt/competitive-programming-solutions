MAX_LEN = 9

t = int(input().strip())

for _ in range(t):
    
    n = int(input().strip())
    
    s = []
    slen = list(map(lambda x: [], [0] * MAX_LEN))
    
    for _ in range(n):
        si = input().strip()
        s.append(si)
        slen[len(si)].append(si)

    # print("ANS: ", end='')
    for i in s:
        exist = False
        for jlen in range(1, len(i)):
            klen = len(i) - jlen
            for j in slen[jlen]:
                for k in slen[klen]:
                    if i == j + k:
                        exist = True
                        break
                if exist:
                    break
            if exist:
                break
        if exist:
            print('1', end='')
        else:
            print('0', end='')
    print()
                        



            
            

