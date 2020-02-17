N = int(input())
A = list(map(int, input().split()))
B = [0]*N
for i in range(N, 0, -1):
    t = B[(i-1)::i]
    s = sum(t) % 2
    B[i-1] = 0 if s == A[i-1] else 1

ans = sum(B)
print(ans)
ans_b = []
if ans > 0:
    for i in range(N):
        if B[i] > 0:
            ans_b.append(str(i+1))
    print(' '.join(ans_b))
