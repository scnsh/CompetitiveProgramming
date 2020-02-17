from collections import deque

N, M = map(int, input().split())
tree = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0]*(N+1)
looped = False


def dfs(x, last_x):
    global looped
    visited[x] = 1
    for i in tree[x]:
        if i != last_x and visited[i] == 1:
            looped = True
        if visited[i] == 0:
            dfs(i, x)


count = 0
remain_points = set(range(1, N+1))
for i in range(1, N+1):
    looped = False
    if visited[i] == 0:
        dfs(i, -1)
        if not looped:
            count += 1
print(count)
