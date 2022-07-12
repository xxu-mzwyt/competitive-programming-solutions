DIGIT = 10

t = int(input().strip())

for _ in range(t):
    
    a = int(input().strip())
    s = list(map(int, input().replace(' ', '')))
    
    for i in range(a):
        for m in input().split(' ')[1]:
            if m == 'U':
                s[i] -= 1
            else:
                s[i] += 1
            s[i] %= DIGIT

    # print("ANS: ", end='')
    print(*s)
