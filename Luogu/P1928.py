def unzip(st):
    
    # print('unzipping', st)
    l = len(st)

    if l < 2 or st.isalpha():
        return st

    if st[0].isdigit():
        for i in range(1, l):
            if not st[:i + 1].isdigit():
                # print('st[i:] is', st[i:])
                return int(st[:i]) * unzip(st[i:])

    for i in range(l):
        if st[i] == '[':
            lbr_cnt = 0
            for j in range(i + 1, l):
                if lbr_cnt == 0 and st[j] == ']':
                    return st[:i] + unzip(st[i + 1:j]) + unzip(st[j + 1:])
                elif st[j] == '[':
                    lbr_cnt += 1
                elif st[j] == ']':
                    lbr_cnt -= 1

    return st

s = input().strip()
print(unzip(s))


