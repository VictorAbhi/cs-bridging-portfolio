import sys
sys.setrecursionlimit(1000000)

N = 875714

# Graphs
G  = [[] for _ in range(N+1)]
GT = [[] for _ in range(N+1)]

# Read file
_, filename = sys.argv
with open(filename) as f:
    for line in f:
        x, y = map(int, line.split())
        G[x].append(y)
        GT[y].append(x)

visited = [False] * (N+1)
finish  = [0] * (N+1)
leader  = [0] * (N+1)

t = 0

# --------- FIRST PASS (on GT) ----------
def dfs_first(start):
    global t
    stack = [(start, 0)]
    while stack:
        node, idx = stack[-1]
        if not visited[node]:
            visited[node] = True

        if idx < len(GT[node]):
            nxt = GT[node][idx]
            stack[-1] = (node, idx + 1)
            if not visited[nxt]:
                stack.append((nxt, 0))
        else:
            stack.pop()
            t += 1
            finish[node] = t

for i in range(N, 0, -1):
    if not visited[i]:
        dfs_first(i)

# --------- SECOND PASS (on G) ----------
visited = [False] * (N+1)

order = sorted(range(1, N+1), key=lambda x: finish[x], reverse=True)

def dfs_second(start):
    stack = [start]
    size = 0
    visited[start] = True
    while stack:
        node = stack.pop()
        size += 1
        for nxt in G[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
    return size

scc_sizes = []

for node in order:
    if not visited[node]:
        scc_sizes.append(dfs_second(node))

scc_sizes.sort(reverse=True)

while len(scc_sizes) < 5:
    scc_sizes.append(0)

print(",".join(map(str, scc_sizes[:5])))
