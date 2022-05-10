n = int(input())

cart_lst = list(map(int, input().split()))

while len(cart_lst) < n:
    for i in list(map(int, input().split())):
        cart_lst.append(i)

step = 0

def mergesort(lst):
    global step;

    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    l = mergesort(lst[:mid])
    r = mergesort(lst[mid:])

    merged = []

    while l and r:
        if l[0] > r[0]:
            merged.append(r[0])
            step += len(l)
            r.remove(r[0])
        else:
            merged.append(l[0])
            l.remove(l[0])


    if l:
        for i in l:
            merged.append(i)
    if r:
        for i in r:
            merged.append(i)

    return merged

# print(mergesort(cart_lst))
mergesort(cart_lst)

print(step)
