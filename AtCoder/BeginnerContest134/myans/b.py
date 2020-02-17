N, D = map(int, input().split())
num = N // (2*D+1)
if N % (2*D+1) > 0:
    print(num+1)
else:
    print(num)
