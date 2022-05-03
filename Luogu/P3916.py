a, c, p, q, r, x = map(int, input().split())

diff1 = (c - a) * p
diff2 = diff1 + q

if a > c:
    print(a + int(x / r))

elif x > diff2:
    print(c + int((x - diff2) / r))

elif x > diff1:
    print(c)

else:
    print(a + int(x / p))

