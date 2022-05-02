a, n, m, x = map(int, input().split())

MAXN = 20


fib = [0, 1]

a_times = [0, 1, 1, 2]
k_times = [0, 0, 0, 0]

for i in range(4, n):
    a_times.append(a_times[-1] + fib[-2])
    k_times.append(k_times[-1] + fib[-1])
    fib.append(fib[-1] + fib[-2])

a_times.append(0)
k_times.append(0)

k = int((m - a_times[n - 1] * a) / k_times[n - 1])

print(a_times[x] * a + k_times[x] * k)



# 1 2 3   4    5     6     7     8
# a k a+k a+2k 2a+3k 3a+5k 5a+8k 8a+13k
# 0 k k   a+k  a+2k  2a+3k 3a+5k 5a+8k
# a 0 a   k    a+k   a+2k  2a+3k 3a+5k
# a a 2a  2a+k 3a+2k 4a+4k 6a+7k 9a+12k
