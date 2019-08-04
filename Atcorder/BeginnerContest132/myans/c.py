N = int(input())
D = list(map(int, input().split()))
d_sorted = sorted(D)

if d_sorted[N//2-1] == d_sorted[N//2]:
  print(0)
else:
  print(d_sorted[N//2] - d_sorted[N//2-1])
