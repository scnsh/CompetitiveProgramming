import math

def is_int(a, b):
  dist = 0
  for i in range(D):
    dist = dist + (a[i] - b[i])**2
  dist = math.sqrt(dist)
  flag = dist.is_integer()
  return flag


N, D = map(int, input().split())
X_list = []
for i in range(N):
  X = list(map(int, input().split()))
  X_list.append(X)

count = 0
for i in range(N):
  for j in range(i+1, N):
    if is_int(X_list[i], X_list[j]):
      count += 1
print(count)