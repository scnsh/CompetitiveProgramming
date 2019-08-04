N = int(input())
A = list(map(int, input().split()))
tmp = A[0]

for i in range(1, N):
  if i % 2 == 0:
    tmp = tmp + A[i]
  else:
    tmp = tmp - A[i]
X = [tmp]*N
for i in range(0, N-1):
  X[i+1] = (A[i] - X[i] // 2) * 2
print(" ".join(list(map(str, X))))