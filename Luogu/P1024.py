a, b, c, d = map(float, input().split())
root_cnt = 0


def fn(vx):
    return a * vx ** 3 + b * vx ** 2 + c * vx + d

def find_root(l, r):

    # print('L=', l, 'R=', r)

    if r - l < 0.005:
        
        print('{:.2f}'.format(l), end=' ')
        return
        
    else:

        m = (l + r) / 2

        l_value = fn(l)
        m_value = fn(m)
        r_value = fn(r)

        if m_value == 0:
            print('{:.2f}'.format(m), end=' ')
            return

        elif l_value * m_value < 0:
            find_root(l, m)

        elif r_value * m_value < 0:
            find_root(m, r)

        else: # l or r is the root, leave it there
            return


for i in range(-100, 100):

    l_value = fn(i)
    r_value = fn(i + 1)

    # print('Lv=', l_value, 'Rv=', r_value)

    if l_value == 0:
        print('{:.2f}'.format(i), end=' ')
        root_cnt += 1

    elif l_value * r_value < 0:
        find_root(i, i + 1)
        root_cnt += 1       

    if root_cnt == 3:
        break
