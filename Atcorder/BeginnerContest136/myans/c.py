N = int(input())
H = list(map(int, input().split()))
res = "Yes"
lenH = len(H)
for i in range(lenH-1, 0, -1):
  add = 0
  if (i < lenH-1 and H[i+1] - H[i] > 1):
    add += 1
    H[i] += 1
  if i > 0 and H[i] < H[i-1]:
    add += 1
    H[i] += 1
  if add > 1:
    res="No"
    break
  if (i < lenH-1 and H[i] > H[i+1]) or (i > 0 and H[i] < H[i-1]):
    res="No"
    break
print(res)