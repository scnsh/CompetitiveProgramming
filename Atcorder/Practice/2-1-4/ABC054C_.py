from collections import deque

N, M = map(int, input().split())
paths = {}
for i in range(1, N+1):
  paths[i]=set()
for i in range(M):
  a, b = map(int, input().split())
  paths[a].add(b)
  paths[b].add(a)

count = 0

def dfs(v, visited):
  global count
  if len(visited) == N:
    count += 1
    return
  for i in paths[v]:
    if i not in visited:
      visited.add(i)
      dfs(i, visited)
      visited.remove(i)
  return

pq = deque()
for i in paths[1]:
  pq.append(i)
  dfs(i, {1, i})
print(count)