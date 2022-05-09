import os
import random

cnt = 0
while True:
    a = random.randint(1000000000000000, 10000000000000000)
    # b = random.randint(1000000000000000, 10000000000000000)
    b = random.randint(100, 1000)
    with open('test.in', 'w') as f:
        f.write(str(a) + '\n' + str(b))
    os.system('P1303.exe<test.in>test.out')
    with open('test.out', 'r') as f:
        ans = int(f.readline().replace(' ', ''))
    if ans != a * b:
        print('ERROR')
        print(a)
        print(b)
        print(ans)
        print(a * b)
        break
    print('test', cnt, 'passed')
    cnt += 1