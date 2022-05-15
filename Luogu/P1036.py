n, k = map(int, input().split())
x = list(map(int, input().split()))

max_sum = sum(x)

is_prime = [False, False] + [True] * max_sum

for i in range(2, max_sum):
    if is_prime[i]:
        for j in range(i * 2, max_sum, i):
            is_prime[j] = False

ways_cnt = 0

def search_ways(depth, curr, lst_sum):

    global ways_cnt

    if depth == k:
        if is_prime[lst_sum]:
            ways_cnt += 1
        return

    for i in range(curr, n):
        search_ways(depth + 1, i + 1, lst_sum + x[i])

search_ways(0, 0, 0)

print(ways_cnt)
    
