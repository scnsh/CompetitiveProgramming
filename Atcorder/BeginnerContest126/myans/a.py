n, k = map(int, input().split())
s = input()
ret = ""
for i, c in enumerate(s):
  ret += c.lower() if i == k-1 else c 
print(ret)