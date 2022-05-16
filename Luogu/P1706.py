n = int(input())

arr = []

def print_arr(depth):

    if depth == n:
        for i in arr:
            print('{:5d}'.format(i), end='')
        print()
        return

    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            print_arr(depth + 1)
            arr.remove(i)

print_arr(0)
