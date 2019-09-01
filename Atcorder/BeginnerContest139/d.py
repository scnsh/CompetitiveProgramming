N = int(input())
N = N-1
if N % 2 == 0:
    print((N+1) * (N//2))
else:
    n = N-1
    print((n+1) * (n//2) + N)
