n, k = map(int, input().split())

tmp = k
count = 0
while tmp > 1:
  tmp = tmp / 2
  count += 1

ret = 0
for i in range(1, n+1):
  goal = pow(2, count) * i
  offset = 0
  if i >= k:
    ret += (1/n)
  else:
    while goal >= k:
      goal = goal / 2
      offset += 1
    a = (1 / n) * pow(0.5, count - (offset-1))
    ret += a
print(ret)