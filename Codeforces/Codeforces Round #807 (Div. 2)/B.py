t = int(input().strip())

for _ in range(t):

    n = int(input().strip())

    rooms = list(map(int, input().split()))

    steps = 0
    
    fstDusty = 0
    fstClean = 0

    while fstDusty < n and rooms[fstDusty] == 0:
        fstDusty += 1
        fstClean += 1
    
    while True:
        
        while fstClean < n and rooms[fstClean] > 0:
            fstClean += 1
        if fstClean == n:
            steps += sum(rooms[:-1])
            break
        
        rooms[fstDusty] -= 1
        rooms[fstClean] += 1
        steps += 1
    
        while rooms[fstDusty] == 0:
            fstDusty += 1

    print(steps)







