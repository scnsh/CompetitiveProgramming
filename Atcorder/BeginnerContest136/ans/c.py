N = int(input())
H = list(map(int, input().split()))
res = "Yes"
lenH = len(H)
val = 0
for i in range(lenH):
  if val <= H[i]-1:
    val = H[i]-1
  elif val == H[i]:
    val = H[i]
  else:
    res = "No"
    break
print(res)
