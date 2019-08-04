N, M = map(int, input().split())
l_max = 1
r_min = N
for _ in range(M):
  l, r = map(int, input().split())
  l_max = l if l > l_max else l_max
  r_min = r if r < r_min else r_min
if r_min - l_max >= 0:
  print(r_min - l_max + 1) 
else:
  print("0")