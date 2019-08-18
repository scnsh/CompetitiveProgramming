N, Q = map(int, input().split())
tree = [[] for i in range(N)]

for i in range(N-1):
  a, b = map(int, input().split())
  tree[a-1].extend([b])

nodes = [0]*N
for _ in range(Q):
  p, x = map(int, input().split())
  nodes[p-1]+=x

for i in range(N-1):
  for j in tree[i]:
    nodes[j-1]+=nodes[i]
print(" ".join(list(map(str, nodes))))