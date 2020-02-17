A, B, C = map(int, input().split())
ret = C - (A - B)
if ret >= 0:
    print(ret)
else:
    print(0)
