import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
g = {}
nodes = set()

for _ in range(n):
    a, op, b = sys.stdin.readline().split()
    if op == '>':
        u, v = a, b
    else:
        u, v = b, a

    if u not in g:
        g[u] = []
    g[u].append(v)
    nodes.add(u)
    nodes.add(v)

vis = {}
ok = True

def dfs(u):
    global ok
    vis[u] = 1
    for v in g.get(u, []):
        if v not in vis:
            dfs(v)
        elif vis[v] == 1:
            ok = False
    vis[u] = 2

for x in nodes:
    if x not in vis:
        dfs(x)

print("possible" if ok else "impossible")