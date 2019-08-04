a, b = map(int, input().split())
if 13 > a:
  if a >= 6:
    print(b//2)
  else:
    print("0")
else:
  print(b)