S = list(input())
count = 1
target = ""
current, remain  = S[0], S[1:]
for i in range(1, len(S)):
  target += S[i]
  if current != target:
    count+=1
    current = target
    target=""
print(count)