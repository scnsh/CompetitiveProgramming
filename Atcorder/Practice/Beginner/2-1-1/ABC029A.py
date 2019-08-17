N = int(input())
tlist = []
for i in range(N):
  t = int(input())
  tlist.append(t)
minimum = sum(tlist)
for i in range(2**N):
  binary=format(i, 'b').zfill(N+2)[2:]
  a1=a2=0
  for i in range(N):
    if binary[i] == '0':
      a1 += tlist[i]
    else:
      a2 += tlist[i]
  if minimum > max(a1,a2):
    minimum = max(a1,a2)
print(minimum)