N, M = map(int, input().split())
A = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(M)]

A.sort()
l = sorted(l, key=lambda x: x[1])

ind = 0
for b, c in l[::-1]:
    mx = min(N, ind+b)
    for i in range(ind, mx):
        if c > A[i]:
            A[i] = c
    if mx == N:
        break
    ind += b
print(sum(A))
