R, G, B, N = map(int, input().split())
count = 0
for r in range(0, N+1, R):
  for g in range(0, N+1-r, G):
    val = (N - r - g)
    if val % B == 0 and val >= 0:
      count += 1
print(count)