N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ret = 0
last_i = N
for n in range(N):
    i = A[n]-1
    ret += B[i]
    if n > 0 and i - last_i == 1:
        ret += C[last_i]
    last_i = i
print(ret)
