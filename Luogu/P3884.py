n = int(input().strip())

edges = list(map(lambda x: [], [0] * (n + 1)))
father = [0] * (n + 1)
depth = [0] * (n + 1)
width = [0] * (n + 1)

for _ in range(n - 1):
    p, c = map(int, input().split())
    edges[p].append((p, c))

a, b = map(int, input().split())

def dfs(curr):
    for i in edges[curr]:
        depth[i[1]] = depth[curr] + 1
        width[depth[i[1]]] += 1
        father[i[1]] = curr
        dfs(i[1])

def find_lca(x, y):
    if x == y:
        return x
    elif depth[x] > depth[y]:
        return find_lca(father[x], y)
    elif depth[x] < depth[y]:
        return find_lca(x, father[y])
    else:
        return find_lca(father[x], father[y])

depth[1] = 1
dfs(1)

# print(depth)
# print(find_lca(a, b))

print(max(depth))
print(max(width))
print(2 * depth[a] + depth[b] - 3 * depth[find_lca(a, b)])



